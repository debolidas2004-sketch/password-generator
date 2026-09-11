import random
import string

length = int(input("Enter password length: "))

if length < 4:
    print("Password length must be at least 4")
else:
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    number = random.choice(string.digits)
    special = random.choice(string.punctuation)

    characters = string.ascii_letters + string.digits + string.punctuation

    password = uppercase + lowercase + number + special

    for i in range(length - 4):
        password += random.choice(characters)

    password = list(password)
    random.shuffle(password)

    password = ''.join(password)

    print("Generated Password:", password)
