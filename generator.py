import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special):
    """
    Generate a secure random password based on user preferences.
    
    Args:
        length (int): Length of the password.
        include_uppercase (bool): Include uppercase letters.
        include_numbers (bool): Include numbers.
        include_special (bool): Include special characters.
    
    Returns:
        The generated password in string 
    """
    
    # Possible characters for the password
    lowercase = string.ascii_lowercase 
    uppercase = '' 
    numbers = ''  
    special = ''  

    # Uppercase letters if the user picks them
    if include_uppercase:
        uppercase = string.ascii_uppercase
    # Add numbers if the user picks them
    if include_numbers:
        numbers = string.digits
    # Add special characters if the user picks them
    if include_special:
        special = string.punctuation

    # Combine selected character types
    all_characters = lowercase + uppercase + numbers + special

    # Check if the user selected at least one character type
    if not all_characters:
        return "Error: You must include at least one character type!"

    # An empty list
    password_characters = []
    
    # Use a loop to pick random characters and add them to the list
    for _ in range(length):
        random_character = random.choice(all_characters)
        password_characters.append(random_character)
    # Joins list of characters into a single string 
    password = ''.join(password_characters)
    return password

def main():
    print("Welcome to the Password Generator!")
    print("Follow the prompts to create a secure password.\n")

    try:
        # Get user input
        length = int(input("Enter the desired password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4. Please try again.")
            return

        include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Generate password
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        
        # Display result
        if "Error" in password:
            print(password)
        else:
            print("\nYour secure password is:")
            print(f">>> {password} <<<")

    except ValueError:
        print("Error: Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
