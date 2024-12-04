import time

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def caesar_decrypt(message, key):
    decrypted_result = ""

    for char in message:
        if char in ALPHABET:
            alphabetic_index = ALPHABET.index(char)
            new_index = (alphabetic_index - key) % len(ALPHABET)
            decrypted_result += ALPHABET[new_index]
        else:
            decrypted_result += char

    return decrypted_result


def crack_caesar_cipher(ciphertext):
    possible_messages = []

    for key in range(len(ALPHABET)):
        decrypted_message = caesar_decrypt(ciphertext, key)
        possible_messages.append((key, decrypted_message))

    return possible_messages


def main():
    ciphertext = input("Enter the ciphertext: ").lower()

    start_time = time.time()
    possible_messages = crack_caesar_cipher(ciphertext)
    end_time = time.time()

    execution_time = end_time - start_time

    print(f"Execution time: {execution_time:.6f} seconds")
    print("Possible messages:")
    for key, message in possible_messages:
        print(f"Key {key}: {message}")


if __name__ == "__main__":
    main()
