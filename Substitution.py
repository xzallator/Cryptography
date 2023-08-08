def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = key[ord(char) - ord('A')].upper()
            else:
                encrypted_char = key[ord(char) - ord('a')]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(key.upper().index(char) + ord('A'))
            else:
                decrypted_char = chr(key.index(char) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


def main():
    key = input("Masukkan kunci penggantian (26 huruf unik): ").lower()
    if len(key) != 26 or not key.isalpha() or len(set(key)) != 26:
        print("Kunci harus berisi 26 huruf unik (a-z atau A-Z).")
        return

    while True:
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Ganti Kunci")
        print("4. Keluar")
        choice = int(input("Pilih tindakan (1/2/3/4): "))

        if choice == 1:
            plaintext = input("Masukkan teks yang ingin dienkripsi: ")
            encrypted_text = encrypt(plaintext, key)
            print("Hasil enkripsi:", encrypted_text)
        elif choice == 2:
            encrypted_text = input("Masukkan teks yang ingin didekripsi: ")
            decrypted_text = decrypt(encrypted_text, key)
            print("Hasil dekripsi:", decrypted_text)
        elif choice == 3:
            key = input("Masukkan kunci penggantian baru (26 huruf unik): ").lower()
            if len(key) != 26 or not key.isalpha() or len(set(key)) != 26:
                print("Kunci harus berisi 26 huruf unik (a-z atau A-Z).")
                continue
            print("Kunci penggantian baru:", key)
        elif choice == 4:
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


if __name__ == "__main__":
    main()
