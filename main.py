import random
import string

def generate_password(length, lower_case, upper_case,special_char,numbers):
    characters = " "
    if upper_case:
        characters += string.ascii_uppercase
    if lower_case:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_char:
        characters += string.punctuation

    if not characters:
        return "At least one character set must be selected"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("enter the length of password: "))
    lower_case = input("include lower_case? (y/n) : ").lower() == "y"
    upper_case = input("include upper_case? (y/n) : ").lower() == "y"
    numbers = input("include numbers? (y/n) : ").lower() == "y"
    special_char = input("include special_char? (y/n) : ").lower() == "y"

    password = generate_password(length,lower_case,upper_case,numbers,special_char)
    print("Generate Password:", password)


