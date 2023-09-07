import random
import string

def generate_password(length):
    # Define characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choices
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    try:
        # Get desired password length from the user
        length = int(input("Enter desired password length: "))
        
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            # Generate the password
            password = generate_password(length)
            
            # Display the generated password
            print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
