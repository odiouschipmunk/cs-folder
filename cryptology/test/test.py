import caesar
import substitution
import vigenere
import letter_frequency
import detect_english
import random
import string
from tqdm import tqdm
import itertools

def brute_force_caesar(input_text):
    highest_score=0
    decrypt=""
    k=0
    results = []
    for key in tqdm(range(1, 26)):  # Caesar cipher keys range from 1 to 25
        decrypted_text = caesar.decrypt(input_text, key)
        score=detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score>highest_score:
            highest_score=score
            decrypt=decrypted_text
            k=key
            results.append((highest_score, k, decrypt))
    print(f'highest score for caesar:{highest_score}\ndecrypted text:{decrypt}\nkey:{k}')
    return results



def test_brute_force_substitution(input_text):
    results = []
    highest_score = 0
    decrypt = ""
    k = 0
    alphabet = string.ascii_lowercase
    
    # Limit to the first 1000 permutations
    top_keys = list(itertools.permutations(alphabet))[:1000]
    
    for key in tqdm([''.join(p) for p in top_keys]):
        decrypted_text = substitution.decrypt(input_text, key)
        score = detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score > highest_score:
            highest_score = score
            decrypt = decrypted_text
            k = key
            results.append((highest_score, decrypt, k))
    
    print(f'highest score for substitution: {highest_score}\ndecrypted text: {decrypt}\nkey: {k}')
    return results


def brute_force_substitution(input_text):
    results = []
    highest_score=0
    decrypt=""
    k=0
    alphabet = string.ascii_lowercase
    
    for key in tqdm([''.join(p) for p in itertools.permutations(alphabet)]):
        decrypted_text = substitution.decrypt(input_text, key)
        score=detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score>highest_score:
            highest_score=score
            decrypt=decrypted_text
            k=key
            results.append((highest_score, decrypt, k))
    print(f'highest score for substitution:{highest_score}\ndecrypted text:{decrypt}\nkey:{k}')
    return results

def test_brute_force_vigenere(input_text):
    results = []
    # Assuming keys are words of length 1 to 5 for simplicity
    alphabet = string.ascii_lowercase
    highest_score=0
    decrypt=""
    k=0
    for key in tqdm([''.join(p) for p in itertools.product(alphabet, repeat=3)]):
        decrypted_text = vigenere.decrypt(input_text, key)
        score=detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score>highest_score:
            highest_score=score
            decrypt=decrypted_text
            k=key
            results.append((highest_score, decrypt, k))
    print(f'highest score for vigenere:{highest_score}\ndecrypted text:{decrypt}\nkey:{k}')
    return results


def brute_force_vigenere(input_text):
    results = []
    # Assuming keys are words of length 1 to 5 for simplicity
    alphabet = string.ascii_lowercase
    highest_score=0
    decrypt=""
    k=0
    for length in range(1,10):
        for key in tqdm([''.join(p) for p in itertools.product(alphabet, repeat=length)]):
            decrypted_text = vigenere.decrypt(input_text, key)
            score=detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
            if score>highest_score:
                highest_score=score
                decrypt=decrypted_text
                k=key
                results.append((highest_score, decrypt, k))
    print(f'highest score for vigenere:{highest_score}\ndecrypted text:{decrypt}\nkey:{k}')
    return results

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
        # Choose the cipher method
        total_results=[[]]
        total_results.append(brute_force_caesar(input_text))
        total_results.append(brute_force_vigenere(input_text))
        total_results.append(brute_force_substitution(input_text))

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