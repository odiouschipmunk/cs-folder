ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message, key):
    key = key.lower()
    encrypted_result = ""
    key_index = 0
    for char in message:
        if char in ALPHABET:
            shift = ALPHABET.index(key[key_index % len(key)])
            new_index = (ALPHABET.index(char) + shift) % len(ALPHABET)
            encrypted_result += ALPHABET[new_index]
            key_index += 1
        else:
            encrypted_result += char
    return encrypted_result

def decrypt(message, key):
    key = key.lower()
    decrypted_result = ""
    key_index = 0
    for char in message:
        if char in ALPHABET:
            shift = ALPHABET.index(key[key_index % len(key)])
            new_index = (ALPHABET.index(char) - shift) % len(ALPHABET)
            decrypted_result += ALPHABET[new_index]
            key_index += 1
        else:
            decrypted_result += char
    return decrypted_result