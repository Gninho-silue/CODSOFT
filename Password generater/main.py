import random
import string

def generate_password(length):
    # Define characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by selecting random characters from the defined set
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
