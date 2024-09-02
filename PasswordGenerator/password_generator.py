import random
import string

def generate_password(length=12):
    """Generate a random password with the given length."""
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the length of the password (default is 12): "))
    except ValueError:
        length = 12

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
