import caesar
import substitution
import vigenere
import letter_frequency
import detect_english
import random
import string
from tqdm import tqdm
import itertools

def brute_force_caesar(input_text):
    highest_score=0
    decrypt=""
    k=0
    results = []
    for key in tqdm(range(1, 26)):  # Caesar cipher keys range from 1 to 25
        decrypted_text = caesar.decrypt(input_text, key)
        score=detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score>highest_score:
            highest_score=score
            decrypt=decrypted_text
            k=key
            results.append((highest_score, k, decrypt))
    print(f'highest score for caesar:{highest_score}\ndecrypted text:{decrypt}\nkey:{k}')
    return results



def test_brute_force_substitution(input_text):
    results = []
    highest_score = 0
    decrypt = ""
    k = 0
    alphabet = string.ascii_lowercase
    
    # Limit to the first 1000 permutations
    top_keys = list(itertools.permutations(alphabet))[:1000]
    
    for key in tqdm([''.join(p) for p in top_keys]):
        decrypted_text = substitution.decrypt(input_text, key)
        score = detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score > highest_score:
            highest_score = score
            decrypt = decrypted_text
            k = key
            results.append((highest_score, decrypt, k))
    
    print(f'highest score for substitution: {highest_score}\ndecrypted text: {decrypt}\nkey: {k}')
    return results


def brute_force_substitution(input_text):
    results = []
    highest_score=0
    decrypt=""
    k=0
    alphabet = string.ascii_lowercase
    
    for key in tqdm([''.join(p) for p in itertools.permutations(alphabet)]):
        decrypted_text = substitution.decrypt(input_text, key)
        score=detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score>highest_score:
            highest_score=score
            decrypt=decrypted_text
            k=key
            results.append((highest_score, decrypt, k))
    print(f'highest score for substitution:{highest_score}\ndecrypted text:{decrypt}\nkey:{k}')
    return results

def test_brute_force_vigenere(input_text):
    results = []
    # Assuming keys are words of length 1 to 5 for simplicity
    alphabet = string.ascii_lowercase
    highest_score=0
    decrypt=""
    k=0
    for key in tqdm([''.join(p) for p in itertools.product(alphabet, repeat=3)]):
        decrypted_text = vigenere.decrypt(input_text, key)
        score=detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
        if score>highest_score:
            highest_score=score
            decrypt=decrypted_text
            k=key
            results.append((highest_score, decrypt, k))
    print(f'highest score for vigenere:{highest_score}\ndecrypted text:{decrypt}\nkey:{k}')
    return results


def brute_force_vigenere(input_text):
    results = []
    # Assuming keys are words of length 1 to 5 for simplicity
    alphabet = string.ascii_lowercase
    highest_score=0
    decrypt=""
    k=0
    for length in range(1,10):
        for key in tqdm([''.join(p) for p in itertools.product(alphabet, repeat=length)]):
            decrypted_text = vigenere.decrypt(input_text, key)
            score=detect_english.is_english(decrypted_text, detect_english.dictionary, return_score=True)
            if score>highest_score:
                highest_score=score
                decrypt=decrypted_text
                k=key
                results.append((highest_score, decrypt, k))
    print(f'highest score for vigenere:{highest_score}\ndecrypted text:{decrypt}\nkey:{k}')
    return results
