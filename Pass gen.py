import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ''
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        print("Error: No character types selected.")
        return None

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def get_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'.")

def main():
    print("=== Random Password Generator ===")

    # Get password length
    while True:
        try:
            length = int(input("Enter password length (e.g., 8): "))
            if length < 1:
                print("Length must be at least 1.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Get character type preferences
    use_letters = get_yes_no("Include letters?")
    use_numbers = get_yes_no("Include numbers?")
    use_symbols = get_yes_no("Include symbols?")

    # Generate and display password
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
