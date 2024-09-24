# Import necessary modules
import caesar
import substitution
import vigenere
import letter_frequency
import detect_english

def main():
    # Read input from a text file
    with open('input.txt', 'r') as file:
        input_text = file.read().strip()

    # Choose the cipher method
    cipher_method = input("Choose the cipher method (caesar, substitution, vigenere): ").lower()

    # Encrypt or decrypt based on user choice
    action = input("Do you want to encrypt or decrypt the message? (encrypt/decrypt): ").lower()

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
        key = input("Enter the Vigenere cipher key: ")
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
    is_english = detect_english.is_english(output_text)

    # Print results
    print("Output text written to output.txt")
    print("Letter Frequency:", letter_freq)
    print("Is the text English?", is_english)

if __name__ == "__main__":
    main()