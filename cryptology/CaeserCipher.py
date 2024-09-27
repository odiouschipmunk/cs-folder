# File: caesar_cipher.py

def encrypt(text, shift):
    """
    Encrypt the text using Caesar Cipher with the specified shift.
    """
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine if the letter is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97

            # Perform the shift
            encrypted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabet characters remain the same

    return encrypted_text


def decrypt(text, shift):
    """
    Decrypt the text using Caesar Cipher with the specified shift.
    """
    return encrypt(text, -shift)


if __name__ == "__main__":
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please choose either 'e' for encryption or 'd' for decryption.")
