import random
import string 

def generate_password(length=12, include_numbers=False, include_characters=False, include_symbols=False):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_characters:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))
