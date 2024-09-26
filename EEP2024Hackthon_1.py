def greet_user(name):
    """Greet the user with their name."""
    if name.lower() == "admin":
        print("Hello, Admin! You have special privileges.")
    else:
        print(f"Hello, {name}! Welcome to the program.")

def count_letters(name):
    """Count the number of letters in the user's name."""
    letter_count = len(name)
    print(f"Your name has {letter_count} letters.")

def main():
    """Main function to run the program."""
    user_name = input("Please enter your name: ")
    greet_user(user_name)
    count_letters(user_name)

if __name__ == "__main__":
    main()
