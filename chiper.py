def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


def main():
    while True:
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        choice = int(input("Pilih tindakan (1/2/3): "))

        if choice == 1:
            plaintext = input("Masukkan teks yang ingin dienkripsi: ")
            shift_key = int(input("Masukkan kunci geser: "))
            encrypted_text = encrypt(plaintext, shift_key)
            print("Hasil enkripsi:", encrypted_text)
        elif choice == 2:
            encrypted_text = input("Masukkan teks yang ingin didekripsi: ")
            shift_key = int(input("Masukkan kunci geser: "))
            decrypted_text = decrypt(encrypted_text, shift_key)
            print("Hasil dekripsi:", decrypted_text)
        elif choice == 3:
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


if __name__ == "__main__":
    main()
