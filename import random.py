import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not any([use_lowercase, use_uppercase, use_digits, use_symbols]):
        return "At least one character type should be selected for password generation."
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_user_input():
    print("Please provide the following information:")
    length = int(input("Enter password length (min 4, max 64): "))
    if length < 4 or length > 64:
        print("Password length out of range. Setting default length to 12.")
        length = 12
    
    use_lowercase = input("Use lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Use digits? (yes/no): ").lower() == 'yes'
    use_symbols = input("Use symbols? (yes/no): ").lower() == 'yes'
    return length, use_lowercase, use_uppercase, use_digits, use_symbols

def display_generated_password(password):
    print("\nGenerated Password:", password)

def main():
    print("Welcome to the Random Password Generator!")
    length, use_lowercase, use_uppercase, use_digits, use_symbols = get_user_input()
    generated_password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
    display_generated_password(generated_password)

if __name__ == "__main__":
    main()
