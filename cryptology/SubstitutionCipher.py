# substitution cipher
# The user will supply an alphabet as a key.
import random

# You will need to write the methods to encode and decode given a key.
# -------------------------------------------------------------------
def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    # To look at every letter in a message
    for letter in message:
        # To find the spot of a letter
        spot = alpha.find(letter)  # this is the numbered spot (0 - 25) of your letter in the alphabet.
        # To print the spot letter in the key
        if spot >= 0:
            secret += key[spot]
        else:
            secret += letter

    return secret


def decode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    plaintext = ""

    # Reverse the key lookup process
    for letter in message:
        spot = key.find(letter)  # find the letter's spot in the key
        if spot >= 0:
            plaintext += alpha[spot]  # map it back to the original alphabet
        else:
            plaintext += letter

    return plaintext


# --------------------------------------------------------------------

# Generates a key using a password.
# The first letters of the alphabet come from the password. Duplicate letters are ignored
# The remaining letters of the alphabet are placed in order to generate the key
def generatePasswordKey(password=""):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = password.upper()
    key = ""

    for letter in password:
        if key.find(letter) == -1:  # letter not yet in key
            key += letter

    for letter in alpha:
        if key.find(letter) == -1:  # letter not yet in key
            key += letter

    return key


# Generates a random permutation of the alphabet and returns the key.
def generateRandomKey():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ""
    alphaList = []

    for letter in alpha:
        alphaList.append(letter)

    random.shuffle(alphaList)

    for letter in alphaList:
        key += letter

    return key

def decrypt(de, key):
    
    if(decode(de, key) == message):
        print("Decryption is correct")
        return "True. Key:"+key+" Message:"+message+" Decoded:"+decode(de, key)
    return "False. Key:"+key+" Message:"+message+" Decoded:"+decode(de, key)
message=""
def main():
    message = input("Enter a message: ")
    
    key = input("Enter a key (leave blank for random key): ")

    if not key:
        key = generateRandomKey()
        print("Generated Key:", key)
    else:
        key = key.upper()  # ensure the key is uppercase

    secret = encode(message, key)
    print("Encrypted:", secret)

    plaintext = decode(secret, key)
    print("decoded:", plaintext)
    while True:
        s=decrypt(secret, generateRandomKey())
        if(s.contains("True")):
            print(s)
            break
        else:
            print("Decryption failed with"+s)

main()
