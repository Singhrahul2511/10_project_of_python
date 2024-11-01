import random
import string

def generate_password(length, include_special, include_numbers, include_uppercase, include_lowercase):
    # Define possible character sets
    special_chars = string.punctuation
    number_chars = string.digits
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase

    # Create a pool of characters to choose from based on user preferences
    possible_characters = ""
    if include_special:
        possible_characters += special_chars
    if include_numbers:
        possible_characters += number_chars
    if include_uppercase:
        possible_characters += uppercase_chars
    if include_lowercase:
        possible_characters += lowercase_chars

    # Generate a random password by selecting characters from the pool
    password = ''.join(random.choice(possible_characters) for _ in range(length))
    
    return password

# User input for password options
length = int(input("Enter password length: "))
include_special = input("Include special characters? (yes/no): ").lower() == "yes"
include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"

# Generate and display the password
password = generate_password(length, include_special, include_numbers, include_uppercase, include_lowercase)
print("Generated Password:", password)
