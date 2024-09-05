import string


def check_pass_strength(password):
    special_characters = string.punctuation
    if len(password) < 8:
        return "Weak"
    elif not any(char.isdigit() for char in password):
        return "Moderate"
    elif not any(char.isupper() for char in password):
        return "Moderate"
    elif not any(char in special_characters for char in password):
        return "Moderate"
    
    else:
        return "Strong"
    
    
pass_strength = check_pass_strength("Ez2djjeeiotrojfje@")
print(f"Password strength: {pass_strength}")

