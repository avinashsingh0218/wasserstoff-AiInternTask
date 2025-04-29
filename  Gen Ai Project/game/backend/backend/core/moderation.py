import re

# Simple example; for production use, integrate a library or external API.
PROFANITY_LIST = {"badword1", "badword2", "curse", "damn"}

def contains_profanity(text: str) -> bool:
    words = re.findall(r"\b\w+\b", text.lower())
    return any(word in PROFANITY_LIST for word in words)
