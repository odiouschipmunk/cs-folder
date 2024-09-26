alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message, key, alphabet=alphabet):
    key_map = {alphabet[i]: key[i] for i in range(len(alphabet))}
    encrypted_result = "".join([key_map[char] if char in key_map else char for char in message])
    return encrypted_result

def decrypt(message, key, alphabet=alphabet):
    key_map = {key[i]: alphabet[i] for i in range(len(alphabet))}
    decrypted_result = "".join([key_map[char] if char in key_map else char for char in message])
    return decrypted_result