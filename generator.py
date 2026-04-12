import secrets
import string

def generate_password(length=16):
    # Define the possible characters
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all characters
    all_characters = letters + digits + symbols
    
    # Use 'secrets' instead of 'random' for better security
    # It generates cryptographically strong random numbers
    password = ''.join(secrets.choice(all_characters) for i in range(length))
    
    return password

# Simple UI
if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    try:
        user_length = int(input("Enter desired password length: "))
        if user_length < 8:
            print("Warning: Short passwords are easy to crack. Setting to 8.")
            user_length = 8
            
        new_password = generate_password(user_length)
        print(f"\nYour new password is: {new_password}\n")
    except ValueError:
        print("Please enter a valid number for the length.")