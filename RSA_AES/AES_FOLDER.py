import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import urandom

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

def encrypt_folder(input_folder, output_folder, password):
    salt = urandom(16)  # Salt unik untuk setiap enkripsi

    # Membuat direktori output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Menderivasi kunci dari password dan salt
    key = derive_key(password, salt)

    # Loop melalui setiap file di dalam folder input
    for root, dirs, files in os.walk(input_folder):
        for file_name in files:
            input_file_path = os.path.join(root, file_name)
            output_file_path = os.path.join(output_folder, file_name + '.bin')

            # Membuat IV yang unik untuk setiap file
            iv = urandom(16)

            # Enkripsi file
            encrypt_file(input_file_path, output_file_path, key, iv)

    with open(os.path.join(output_folder, 'salt.bin'), 'wb') as salt_file:
        salt_file.write(salt)


def rename_files_in_folder(folder_path, new_name, new_extension):
    # Membuat daftar semua file dalam folder
    files = os.listdir(folder_path)

    # Loop melalui setiap file dan memberikan nama baru
    for i, file_name in enumerate(files):
        

        # Membuat nama baru dengan format "new_name_1", "new_name_2", dst.
        new_file_name = f"{new_name}_{i+1}.{new_extension}"

        # Mengganti nama file
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)
        os.rename(old_path, new_path)

# Contoh penggunaan
folder_path = 'enigfol2'  # Ganti dengan path folder yang ingin dimanipulasi
new_name = 'ENCRYPTED'  # Ganti dengan nama baru yang diinginkan
new_extension = 'dat'

# Memanipulasi nama seluruh file dalam folder
rename_files_in_folder(folder_path, new_name, new_extension)
print("FILE HAVE BEEN MANIPULATED")

# Contoh penggunaan
password = "sha89"  
input_folder = 'enigfol2'  
output_folder = 'encrypted_enigma32'  

# Enkripsi folder
encrypt_folder(input_folder, output_folder, password)
print("FOLDER HAS BEEN ENCRYPTED BY AES")
