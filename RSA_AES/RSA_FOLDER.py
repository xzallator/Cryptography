import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as rsa_padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import urandom

def generate_rsa_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

def encrypt_rsa(public_key, data):
    return public_key.encrypt(
        data,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32  # Panjang kunci AES-256
    )
    return kdf.derive(password.encode('utf-8'))

def encrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(ciphertext)

def encrypt_folder(input_folder, output_folder, public_key, encrypted_prefix='encrypted_'):
    # Generate kunci simetris (AES)
    aes_key = os.urandom(32)

    # Simpan kunci simetris terenkripsi ke file
    encrypted_aes_key = encrypt_rsa(public_key, aes_key)
    with open(os.path.join(output_folder, 'encrypted_aes_key.bin'), 'wb') as key_file:
        key_file.write(encrypted_aes_key)

    # Loop melalui setiap file di dalam folder input
    for i, (root, dirs, files) in enumerate(os.walk(input_folder)):
        for j, file_name in enumerate(files):
            input_file_path = os.path.join(root, file_name)

            # Membuat IV yang unik untuk setiap file
            iv = urandom(16)

            # Menentukan nama file keluaran
            output_file_name = f"{encrypted_prefix}{i * len(files) + j + 1}.dat.enc"
            output_file_path = os.path.join(output_folder, output_file_name)

            # Enkripsi file
            encrypt_file(input_file_path, output_file_path, aes_key, iv)




def main():
    # Generate RSA key pair
    rsa_private_key = generate_rsa_key()
    rsa_public_key = rsa_private_key.public_key()

    # Simpan kunci publik RSA ke file
    with open("public_key.pem", "wb") as key_file:
        key_file.write(rsa_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))


    print("PUBLIC KEY SAVED TO PUBLIC_KEY.pem")

    # Enkripsi folder dengan menggunakan RSA public key
    input_folder = 'targetfold'
    output_folder = 'encrypted_folder88'

    # Membuat direktori output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    encrypt_folder(input_folder, output_folder, rsa_public_key)

    print(f"Folder '{input_folder}' encrypted and saved to '{output_folder}'") 

if __name__ == "__main__":
    main()
