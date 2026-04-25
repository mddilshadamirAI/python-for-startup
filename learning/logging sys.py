import hashlib
import getpass

class AuthSystem:
    def __init__(self):
        # We store the HASH of the password, not the password itself
        self.user_db = {
            "admin": self._hash_password("password123")
        }

    def _hash_password(self, password):
        """Converts a plain password into a secure SHA-256 hash."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if username in self.user_db:
            print("User already exists!")
        else:
            self.user_db[username] = self._hash_password(password)
            print(f"User {username} registered successfully.")

    def authenticate(self, username, password):
        hashed_input = self._hash_password(password)
        if self.user_db.get(username) == hashed_input:
            return True
        return False

# --- Execution ---
if __name__ == "__main__":
    system = AuthSystem()
    print("--- 🏛️ Architect Secure Login ---")
    
    user = input("Username: ")
    pw = getpass.getpass("Password: ")

    if system.authenticate(user, pw):
        print(f"\n✅ Welcome back, {user}! System initialized.")
    else:
        print("\n❌ Access Denied.")
