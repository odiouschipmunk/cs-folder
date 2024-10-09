import random
from math import gcd

# Function to compute the greatest common divisor
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

# Function to find the modular inverse of e mod phi
def modinv(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

# Function to generate RSA keys
def generate_keys():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    # Generate two distinct prime numbers
    def generate_prime():
        while True:
            prime_candidate = random.randint(100, 500)
            if is_prime(prime_candidate):
                return prime_candidate

    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    # e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # finding d (private key) using different values of k
    try:
        d = modinv(e, phi)
    except Exception:
        d = None
        k = 1
        while d is None:
            try:
                d = modinv(e, phi)
            except Exception:
                k += 1
                e = random.randrange(2, phi)
                while gcd(e, phi) != 1:
                    e = random.randrange(2, phi)

    return (e, n), (d, n)

# f to encrypt a message using RSA
def rsa_encrypt(message, public_key):
    e, n = public_key
    return (message ** e) % n

# f to decrypt a message using RSA
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return (ciphertext ** d) % n

# e messages (your example)
def encrypt_message():
    again = "y"
    print("encrypt")
    while again == "y":
        try:
            pt = int(input("message "))
            publicKey = int(input("friend public key"))
            publicMod = int(input("friend public mod "))
            ct = (pt ** publicKey) % publicMod
            print(f"calc: ({pt}^{publicKey}) mod {publicMod}")
            print(f"msg: {ct}")
        except ValueError:
            print("please enter good values")
        
        print("")
        again = input("enc another message? Type 'y' for yes or 'n' for no: ").lower()
        print("")

# Decrypt messages (your example)
def decrypt_message():
    again = "y"
    print("use for decrypt")
    while again == "y":
        try:
            ct = int(input("message sent"))
            privateKey = int(input("your private key"))
            publicMod = int(input("you public mod"))
            pt = (ct ** privateKey) % publicMod
            print(f"calc: ({ct}^{privateKey}) mod {publicMod}")
            print(f"orignal message: {pt}")
        except ValueError:
            print("enter good values pleae")
        
        print("")
        again = input("decrypt? y or n").lower()
        print("")

#?
def rsa_interface():
    public_key, private_key = None, None
    
    while True:
        print("=== RSA Encryption/Decryption Program ===")
        print("1. Generate RSA keys")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Generating RSA keys...")
            public_key, private_key = generate_keys()
            print(f"Public Key: {public_key}")
            print(f"Private Key: {private_key}")
            print(f"Modulus (n): {public_key[1]}")
        
        elif choice == "2":
            if not public_key or not private_key:
                print("You must generate RSA keys first.")
            else:
                encrypt_message()
        
        elif choice == "3":
            if not public_key or not private_key:
                print("You must generate RSA keys first.")
            else:
                decrypt_message()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    rsa_interface()
