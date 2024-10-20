import random
import string

def generate_password(length):
    # Define character sets for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + special

    # Make sure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters from the combined set
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Join the list to form the final password string
    return ''.join(password)

# User input for password length
length = int(input("Enter the desired password length (minimum 4): "))

if length < 4:
    print("Password length must be at least 4 characters.")
else:
    password = generate_password(length)
    print("Generated password:", password)
