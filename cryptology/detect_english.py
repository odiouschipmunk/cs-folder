import re

def is_english(text):
    # Simple heuristic: check if the text contains common English words
    common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i"]
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    matches = sum(1 for word in words if word in common_words)
    return matches / len(words) > 0.1  # Arbitrary threshold