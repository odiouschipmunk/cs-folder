# Python for RSA asymmetric cryptographic algorithm.
# For demonstration, values are
# relatively small compared to practical application
import math

publicMod = 0
publicKey = 0
privateKey = 0
p = q = 0


def gcd(a, h):
    temp = 0
    while 1:
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp


def findPrime(rang):
    possiblePrimes = []
    for num in range(2, rang):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            possiblePrimes.append(num)
    return possiblePrimes


def generatekey():
    p = int(input("Enter the first prime number: "))
    q = int(input("Enter the second prime number: "))
    publicMod = p * q
    phi = (p - 1) * (q - 1)
    print("The value of phi ", phi)
    possibleKeys = []
    for i in range(2, phi):
        if math.gcd(i, phi) == 1:
            possibleKeys.append(i)
    print("Possible Public Keys: ", possibleKeys)
    publicKey = int(input("Choose a Public Key from the list above: "))
    possiblePrivateKeys = []
    for i in range(1, phi):
        if (i * publicKey) % phi == 1:
            possiblePrivateKeys.append(i)
    print("Possible Private Keys: ", possiblePrivateKeys)
    privateKey = int(input("Choose a Private Key from the list above: "))
    print("Public Key: ", publicKey)
    print("Private Key: ", privateKey)
    print("Public Modulus: ", publicMod)


def encrypt():
    generatekey()
    again = "y"
    print(
        "Hello! Use this program to ENCRYPT the messages that you want to send to your friends"
    )
    while again == "y":
        pt = int(input("What is the message you want to send?"))
        publicKey = int(input("What is your FRIEND'S Public Key?"))
        publicMod = int(input("What is your FRIEND'S Public Modulus?"))
        ct = (pt**publicKey) % publicMod
        print(
            "The Calculation: ("
            + str(pt)
            + "^"
            + str(publicKey)
            + ") mod "
            + str(publicMod)
        )
        print("THE SECRET MESSAGE: " + str(ct))
        print("")
        again = input("Encrypt another message? type 'y' or 'n'").lower()
        print("")


def decrypt():
    generatekey()
    phi = (p - 1) * (q - 1)
    # Decrypting Messages!
    again = "y"
    print(
        "Hello! Use this program to DECRYPT the messages that were sent to you from your friends"
    )
    while again == "y":
        ct = int(input("What is the message you were sent?"))
        privateKey = int(input("What is YOUR Private Key?"))
        while privateKey < phi:
            if gcd(privateKey, phi) == 1:
                print("awesome, it works!")
                break
            else:
                privateKey += 1
                print("it doesnt work, going to the next key")
        pt = (ct**privateKey) % publicMod
        print(
            "The Calculation: ("
            + str(ct)
            + "^"
            + str(privateKey)
            + ") mod "
            + str(publicMod)
        )
        print("THE ORIGINAL MESSAGE: " + str(pt))
        print("")
        again = input("Decrypt another message? type 'y' or 'n'").lower()
        print("")


if __name__ == "__main__":
    i = input("encrypt or decrypt e/d")
    if i == "e":
        encrypt()
    else:
        decrypt()
