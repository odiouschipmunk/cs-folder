import string

def generate_cipher(key):
    alphabet = string.ascii_uppercase
    cipher = dict(zip(alphabet, key))
    return cipher

def encrypt(message, cipher):
    message = message.upper()
    encrypted_message = ''.join([cipher.get(letter, letter) for letter in message])
    return encrypted_message

def decrypt(ciphertext, cipher):
    reverse_cipher = {v: k for k, v in cipher.items()}
    decrypted_message = ''.join([reverse_cipher.get(letter, letter) for letter in ciphertext])
    return decrypted_message

key = "BCDA"  
cipher = generate_cipher(key)

plaintext = "ABCD"
ciphertext = encrypt(plaintext, cipher)
print(f"Encrypted: {ciphertext}")

decrypted = decrypt(ciphertext, cipher)
print(f"Decrypted: {decrypted}")
