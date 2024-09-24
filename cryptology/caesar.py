ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message, key):
    encrypted_result = ""
    for char in message:
        if char in ALPHABET:
            new_index = (ALPHABET.index(char) + key) % len(ALPHABET)
            encrypted_result += ALPHABET[new_index]
        else:
            encrypted_result += char
    return encrypted_result

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def decrypt(message, key):
    decrypted_result = ""
    
    for char in message:
        if char in ALPHABET:
            alphabetic_index = ALPHABET.index(char)
            new_index = (alphabetic_index - key) % len(ALPHABET)
            decrypted_result += ALPHABET[new_index]
        else:
            decrypted_result += char
    
    return decrypted_result