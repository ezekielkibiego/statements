import secrets, string
def generate_random_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    # print(characters)
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

random_password = generate_random_password()
print(random_password)