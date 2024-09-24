import caesar
import substitution
import vigenere
import letter_frequency
import detect_english
import random
import string
from tqdm import tqdm
def generate_random_key(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def brute_force_decrypt(input_text):
    best_guess = ""
    best_score = 0
    best_key = None
    best_method = None
    used_keys = set()

    # Brute force Caesar cipher
    for key in range(len(caesar.ALPHABET)):
        decrypted_text = caesar.decrypt(input_text, key)
        score = detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score > best_score:
            best_score = score
            best_guess = decrypted_text
            best_key = key
            best_method = "Caesar"
        if score == 1.0:
            print("Detected English using Caesar cipher with key", key)
            print("Decrypted text:", decrypted_text)
            return

    # Brute force Substitution cipher
    # Assuming we have a list of possible substitution keys
    possible_keys = ["abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"]  # Add more keys as needed
    for key in tqdm(possible_keys):
        decrypted_text = substitution.decrypt(input_text, key)
        score = detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score > best_score:
            best_score = score
            best_guess = decrypted_text
            best_key = key
            best_method = "Substitution"
        if score == 1.0:
            print("Detected English using Substitution cipher with key", key)
            print("Decrypted text:", decrypted_text)
            return
        print('finished substitution')

    # Brute force Vigenere cipher with random keys
    for _ in tqdm(range(1000)):  # Try 1000 random keys
        key_length = 6#random.randint(1, 10)
        key = generate_random_key(key_length)
        while key in used_keys:
            key = generate_random_key(key_length)
        used_keys.add(key)
        decrypted_text = vigenere.decrypt(input_text, key)
        score = detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score > best_score:
            best_score = score
            best_guess = decrypted_text
            best_key = key
            best_method = "Vigenere"
        if score == 1.0:
            print("Detected English using Vigenere cipher with key", key)
            print("Decrypted text:", decrypted_text)
            return

    decrypted_text = vigenere.decrypt(input_text, "woohoo")
    score = detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
    if score > best_score:
        best_score = score
        best_guess = decrypted_text
        best_key = key
        best_method = "Vigenere"
    if score == 1.0:
        print("Detected English using Vigenere cipher with key", "woohoo")
        print("Decrypted text:", decrypted_text)
        return

    # If no perfect match is found, print the best guess
    print("No perfect English match found. Best guess:")
    print("Decryption method:", best_method)
    print("Key:", best_key)
    print("Decrypted text:", best_guess)

def main():
    # Read input from a text file
    with open('input.txt', 'r') as file:
        input_text = file.read().strip()

    # Choose the action
    action = input("Do you want to encrypt, decrypt, or brute force the message? (encrypt/decrypt/brute force): ").lower()

    if action == 'encrypt' or action == 'decrypt':
        # Choose the cipher method
        cipher_method = input("Choose the cipher method (caesar, substitution, vigenere): ").lower()

        if cipher_method == 'caesar':
            key = int(input("Enter the Caesar cipher key: "))
            if action == 'encrypt':
                output_text = caesar.encrypt(input_text, key)
            elif action == 'decrypt':
                output_text = caesar.decrypt(input_text, key)
            else:
                print("Invalid action.")
                return

        elif cipher_method == 'substitution':
            key = input("Enter the substitution cipher key: ")
            if action == 'encrypt':
                output_text = substitution.encrypt(input_text, key)
            elif action == 'decrypt':
                output_text = substitution.decrypt(input_text, key)
            else:
                print("Invalid action.")
                return

        elif cipher_method == 'vigenere':
            key = input("Enter the Vigenere cipher key: ").lower()
            if action == 'encrypt':
                output_text = vigenere.encrypt(input_text, key)
            elif action == 'decrypt':
                output_text = vigenere.decrypt(input_text, key)
            else:
                print("Invalid action.")
                return

        else:
            print("Invalid cipher method.")
            return

        # Write output to a text file
        with open('output.txt', 'w') as file:
            file.write(output_text)

        # Compute letter frequency and detect English
        letter_freq = letter_frequency.compute_frequency(output_text)
        is_english = detect_english.is_english(output_text, detect_english.dictionary)

        # Print results
        print("Output text written to output.txt")
        print("Letter Frequency:", letter_freq)
        print("Is the text English?", is_english)

    elif action == 'brute force':
        brute_force_decrypt(input_text)

    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()