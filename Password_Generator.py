import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "You must select at least one character type!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Password Generator 🔐\n")

    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (e.g. @, #, $)? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    print(f"\nYour generated password is:\n👉 {password}")


if __name__ == "__main__":
    main()
