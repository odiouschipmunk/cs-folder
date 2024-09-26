from collections import Counter

def compute_frequency(text):
    text = text.lower()
    frequency = Counter(text)
    total_letters = sum(frequency[char] for char in frequency if char.isalpha())
    frequency_percentage = {char: (count / total_letters) * 100 for char, count in frequency.items() if char.isalpha()}
    return frequency_percentage