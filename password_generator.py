import random

def create_password(length):
    if length < 4:
        return "Password must be at least 4 characters long."

    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_symbols = "!@#$%^&*"

    password_chars = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(numbers),
        random.choice(special_symbols)
    ]

    all_characters = lowercase_letters + uppercase_letters + numbers + special_symbols

    for _ in range(length - 4):
        password_chars.append(random.choice(all_characters))

    random.shuffle(password_chars)
    return ''.join(password_chars)

def main():
    print("=== Password Generator ===")
    try:
        user_input = input("Enter the password length you want: ")
        password_length = int(user_input)

        while True:
            result = create_password(password_length)
            print("Generated Password:", result)

            again = input("Do you want to generate another password? (yes/no): ").strip().lower()
            if again != "yes":
                print("Thank you for using the password generator.")
                break

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
