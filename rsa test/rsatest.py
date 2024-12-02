import random
import math


# Function to generate prime numbers using Sieve of Eratosthenes
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


# Function to generate good keys (private, public, and public modulus)
def generate_keys(bit_length):
    primes = generate_primes(2 ** (bit_length // 2))
    p = random.choice(primes)
    primes.remove(p)
    q = random.choice(primes)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while math.gcd(e, phi) != 1:
        e += 1

    d = pow(e, -1, phi)

    return (e, n), (d, n)


# Function to encrypt plaintext
def encrypt(plaintext, public_key):
    e, n = public_key
    encrypted_text = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_text


# Function to decrypt ciphertext
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_text = "".join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_text


# Function to allow user to change the bit length of the keys
def change_key_bit_length(bit_length):
    public_key, private_key = generate_keys(bit_length)
    return public_key, private_key


if __name__ == "__main__":
    bit_length = 64  # Default bit length
    public_key, private_key = generate_keys(bit_length)

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("Enter the message to encrypt: ")
    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)

    # Change key bit length
    new_bit_length = int(input("Enter new bit length for keys (e.g., 64, 256): "))
    public_key, private_key = change_key_bit_length(new_bit_length)

    print("New Public Key:", public_key)
    print("New Private Key:", private_key)

    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message with new keys:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message with new keys:", decrypted_message)
