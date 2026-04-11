import random
import string

def generate_password(length=12):
    # Define the characters we want to use
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters from the list 'length' number of times
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password

def main():
    print("--- 🛡️ Quick Password Generator ---")
    
    try:
        user_length = int(input("Enter desired password length: "))
        if user_length < 4:
            print("For security, try a length of at least 4!")
            return
            
        new_password = generate_password(user_length)
        
        print("\nGenerated Password:")
        print(f"👉 {new_password}\n")
        print("Keep it secret, keep it safe!")
        
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()