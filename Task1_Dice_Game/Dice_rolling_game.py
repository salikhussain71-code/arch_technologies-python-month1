import random

print("Welcome to the Dice Rolling Game!")

while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print("\nYou rolled:")
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {die1 + die2}")

    choice = input("\nWould you like to roll again? (yes/no): ")
    choice = choice.strip().lower()

    if choice in ("yes", "y"):
        continue
    elif choice in ("no", "n"):
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice. The game will roll again.")