import caesar
import substitution
import vigenere
import letter_frequency
import detect_english
import random
import string
from tqdm import tqdm
import itertools
import brute_force
def main():
    # Read input from a text file
    with open('input.txt', 'r') as file:
        input_text = file.read().strip()

    # Choose the action
    action = input("Do you want to encrypt, decrypt, or brute force the message? (encrypt/decrypt/brute force/brute force test): ").lower()

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

    elif action == 'brute force test':
        # Choose the cipher method
        total_results=[[]]
        total_results.append(brute_force.brute_force_caesar(input_text))
        total_results.append(brute_force.test_brute_force_vigenere(input_text))
        total_results.append(brute_force.test_brute_force_substitution(input_text))

        with open('brute_force_results.txt', 'w') as file:
            for result in total_results:
                for highest_score, decrypt, k in result:
                    file.write(f"Highest score: {highest_score}\n")
                    file.write(f"Key: {k}\n")
                    file.write(f"Decrypted text: {decrypt}\n\n")
        print("Brute force results written to brute_force_results.txt")
    
    
    
    elif action == 'brute force':
        # Choose the cipher method
        total_results=[[]]
        total_results.append(brute_force.brute_force_caesar(input_text))
        total_results.append(brute_force.brute_force_vigenere(input_text))
        total_results.append(brute_force.brute_force_substitution(input_text))

        with open('brute_force_results.txt', 'w') as file:
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