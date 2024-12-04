# i used the gfg site that you had linked in the test document
primes = []
with open("primes.txt", "r") as f:
    for line in f:
        primes.append(int(line))
p = primes[0]
q = primes[1]
n = p * q  # public mod
phi = (p - 1) * (q - 1)
possible_e = []  # pub key


def find_pub_key():
    for i in range(2, phi):
        if phi % i != 0:
            possible_e.append(i)


find_pub_key()
print(f"found {len(possible_e)} possible public keys")
pub_key = possible_e[-1]
d = 2
possible_priv_keys = []


def find_d():  # find private key
    d = 2
    while len(possible_priv_keys) < 3:
        if (d * pub_key) % phi == 1:
            possible_priv_keys.append(d)
        d += 1


find_d()
priv_key = possible_priv_keys[-1]
print(
    f"found minimum of {len(possible_priv_keys)} possible private keys as : {possible_priv_keys}"
)
public_mod = n
with open("keys.txt", "w") as f:
    f.write(
        f"Public Key: {pub_key}\nPrivate Key: {priv_key}\nPublic Modulus: {public_mod}"
    )


def encrypt(message):
    return pow(message, pub_key, public_mod)


with open("encrypted_phone.txt", "w") as f:
    f.write(
        f"encrypted phone number: {encrypt(640)}"
    )  # last 4 phone numbers are 9640, so i did 640
with open("final_output.txt", "w") as f:
    f.write(
        f"Public Key: {pub_key}\nPrivate Key: {priv_key}\nPublic Modulus: {public_mod}\nencrypted phone number: {encrypt(640)}\nplaintext phone number: 640"
    )


def decrypt(cipher):
    return pow(cipher, priv_key, public_mod)


print(f"decrypted phone number: {decrypt(encrypt(640))}")
