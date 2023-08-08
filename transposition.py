def encrypt(plaintext, key):
    num_columns = len(key)
    num_rows = (len(plaintext) + num_columns - 1) // num_columns
    padding_size = num_rows * num_columns - len(plaintext)

    plaintext += " " * padding_size

    encrypted_text = ""
    for col in key:
        current_index = col
        for row in range(num_rows):
            encrypted_text += plaintext[current_index]
            current_index += num_columns

    return encrypted_text


def decrypt(encrypted_text, key):
    num_columns = len(key)
    num_rows = (len(encrypted_text) + num_columns - 1) // num_columns

    decrypted_text = [''] * len(encrypted_text)
    index = 0
    for col in key:
        current_index = col
        for row in range(num_rows):
            decrypted_text[current_index] = encrypted_text[index]
            index += 1
            current_index += num_columns

    return ''.join(decrypted_text)


def main():
    print("Masukkan kunci Transposition Cipher:")
    key = list(map(int, input("Masukkan urutan kolom yang diinginkan (pisahkan dengan spasi): ").split()))

    while True:
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        choice = int(input("Pilih tindakan (1/2/3): "))

        if choice == 1:
            plaintext = input("Masukkan teks yang ingin dienkripsi: ")
            encrypted_text = encrypt(plaintext, key)
            print("Hasil enkripsi:", encrypted_text)
        elif choice == 2:
            encrypted_text = input("Masukkan teks yang ingin didekripsi: ")
            decrypted_text = decrypt(encrypted_text, key)
            print("Hasil dekripsi:", decrypted_text)
        elif choice == 3:
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


if __name__ == "__main__":
    main()
