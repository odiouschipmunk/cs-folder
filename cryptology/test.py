import caesar
import substitution
import vigenere
import letter_frequency
import detect_english
import random
import string
from tqdm import tqdm


def generate_random_key(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def brute_force_decrypt(input_text):
    best_guess = ""
    best_score = 0
    best_key = None
    best_method = None
    used_keys = set()

    # Brute force Caesar cipher
    for key in tqdm(range(len(caesar.ALPHABET))):  # Try all possible Caesar keys
        decrypted_text = caesar.decrypt(input_text, key)
        score = detect_english.is_english(
            decrypted_text, detect_english.dictionary, return_score=True
        )
        if score > best_score:
            best_score = score
            best_guess = decrypted_text
            best_key = key
            best_method = "Caesar"
        if score == 1.0:
            print("Detected English using Caesar cipher with key", key)
            print("Decrypted text:", decrypted_text)
            return

    # If Caesar cipher decryption is not perfect, proceed to Substitution cipher
    if best_method != "Caesar":
        # Brute force Substitution cipher with random keys
        used_keys.clear()
        for _ in tqdm(range(1000)):  # Try 1000 random keys
            key = "".join(
                random.sample(string.ascii_lowercase, len(string.ascii_lowercase))
            )
            while key in used_keys:
                key = "".join(
                    random.sample(string.ascii_lowercase, len(string.ascii_lowercase))
                )
            used_keys.add(key)
            decrypted_text = substitution.decrypt(input_text, key)
            score = detect_english.is_english(
                decrypted_text, detect_english.dictionary, return_score=True
            )
            if score > best_score:
                best_score = score
                best_guess = decrypted_text
                best_key = key
                best_method = "Substitution"
            if score == 1.0:
                print("Detected English using Substitution cipher with key", key)
                print("Decrypted text:", decrypted_text)
                return

    # If neither Caesar nor Substitution cipher decryption is perfect, proceed to Vigenere cipher
    if best_method not in ["Caesar", "Substitution"]:
        # Brute force Vigenere cipher with random keys of length 6
        used_keys.clear()
        for _ in tqdm(range(1000)):  # Try 1000 random keys
            key = generate_random_key(6)
            while key in used_keys:
                key = generate_random_key(6)
            used_keys.add(key)
            decrypted_text = vigenere.decrypt(input_text, key)
            score = detect_english.is_english(
                decrypted_text, detect_english.dictionary, return_score=True
            )
            if score > best_score:
                best_score = score
                best_guess = decrypted_text
                best_key = key
                best_method = "Vigenere"
            if score == 1.0:
                print("Detected English using Vigenere cipher with key", key)
                print("Decrypted text:", decrypted_text)
                return

    # If no perfect match is found, print the best guess
    print("No perfect English match found. Best guess:")
    print("Decryption method:", best_method)
    print("Key:", best_key)
    print("Decrypted text:", best_guess)


def main():
    # Read input from a text file
    with open("input.txt", "r") as file:
        input_text = file.read().strip()

    # Choose the action
    action = input(
        "Do you want to encrypt, decrypt, or brute force the message? (encrypt/decrypt/brute force): "
    ).lower()

    if action == "encrypt" or action == "decrypt":
        # Choose the cipher method
        cipher_method = input(
            "Choose the cipher method (caesar, substitution, vigenere): "
        ).lower()

        if cipher_method == "caesar":
            key = int(input("Enter the Caesar cipher key: "))
            if action == "encrypt":
                output_text = caesar.encrypt(input_text, key)
            elif action == "decrypt":
                output_text = caesar.decrypt(input_text, key)
            else:
                print("Invalid action.")
                return

        elif cipher_method == "substitution":
            key = input("Enter the substitution cipher key: ")
            if action == "encrypt":
                output_text = substitution.encrypt(input_text, key)
            elif action == "decrypt":
                output_text = substitution.decrypt(input_text, key)
            else:
                print("Invalid action.")
                return

        elif cipher_method == "vigenere":
            key = input("Enter the Vigenere cipher key: ").lower()
            if action == "encrypt":
                output_text = vigenere.encrypt(input_text, key)
            elif action == "decrypt":
                output_text = vigenere.decrypt(input_text, key)
            else:
                print("Invalid action.")
                return

        else:
            print("Invalid cipher method.")
            return

        # Write output to a text file
        with open("output.txt", "w") as file:
            file.write(output_text)

        # Compute letter frequency and detect English
        letter_freq = letter_frequency.compute_frequency(output_text)
        is_english = detect_english.is_english(output_text, detect_english.dictionary)

        # Print results
        print("Output text written to output.txt")
        print("Letter Frequency:", letter_freq)
        print("Is the text English?", is_english)

    elif action == "brute force":
        # Choose the cipher method
        total_results = [[]]
        total_results.append(brute_force.brute_force_caesar(input_text))
        total_results.append(brute_force.brute_force_vigenere(input_text))
        total_results.append(brute_force.brute_force_substitution(input_text))

        with open("brute_force_results.txt", "w") as file:
            for result in total_results:
                for highest_score, decrypt, k in result:
                    file.write(f"Highest score: {highest_score}\n")
                    file.write(f"Key: {k}\n")
                    file.write(f"Decrypted text: {decrypt}\n\n")
        print("Brute force results written to brute_force_results.txt")

    else:
        print("Invalid action.")


if __name__ == "__main__":
    main()
