# VigenereCipher.py
from CaeserCipher import encrypt, decrypt
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def findKey(keyword, letterCount):
    keyword = keyword.upper()
    spot = letterCount % len(keyword)
    key = alpha.find(keyword[spot])
    return key

def encode_vigenere(message, keyword):
    secret = ""
    letterCount = 0

    message = message.upper()
    for letter in message:
        key = findKey(keyword, letterCount)

        if alpha.find(letter) >= 0:  # check if the letter is alphabetic
            encrypted_letter = encrypt(letter, key)  # Using Caesar Cipher's encrypt method
            secret += encrypted_letter
            letterCount += 1
        else:
            secret += letter  # Non-alphabetic characters remain unchanged

    return secret


def decode_vigenere(message, keyword):
    secret = ""
    letterCount = 0

    message = message.upper()
    for letter in message:
        key = findKey(keyword, letterCount)

        if alpha.find(letter) >= 0:
            decrypted_letter = decrypt(letter, key)  # Using Caesar Cipher's decrypt method
            secret += decrypted_letter
            letterCount += 1
        else:
            secret += letter

    return secret

def main():
    mode = input("Do you want to (e)ncode or (d)ecode? ").lower()
    message = input("Enter message: ")
    keyword = input("Enter keyword: ")

    if mode == 'e':
        encoded_message = encode_vigenere(message, keyword)
        print("Encoded message:", encoded_message)
    elif mode == 'd':
        decoded_message = decode_vigenere(message, keyword)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid mode. Choose 'e' for encode or 'd' for decode.")

if __name__ == "__main__":
    main()
