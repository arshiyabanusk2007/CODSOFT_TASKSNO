import random
import string

print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8!")
            continue

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        print("\nGenerated Password:", password)
        print("Password generated successfully!")

        choice = input("\nGenerate another password? (yes/no): ").lower()

        if choice != "yes":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number!")
