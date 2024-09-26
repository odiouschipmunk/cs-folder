import re

# Load the dictionary from the file
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return set(word.lower() for word in words)
# Load the dictionary once when the module is imported
dictionary = load_dictionary('dictionary.txt')
# Check if the text is English based on the dictionary
def is_english(text, dictionary, threshold=0.5, return_score=False):
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return False if not return_score else 0
    matches = sum(1 for word in words if word in dictionary)
    score = matches / len(words)
    if return_score:
        return score
    return score >= threshold

