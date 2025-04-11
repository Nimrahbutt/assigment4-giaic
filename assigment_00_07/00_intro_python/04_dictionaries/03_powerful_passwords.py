import hashlib

# Function to hash a password using SHA-256
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify login
def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    # Hash the provided password
    hashed_password = hash_password(password_to_check)
    
    # Check if email exists and hashes match
    return stored_logins.get(email) == hashed_password

# Example usage
def main():
    # Simulated database with hashed passwords
    stored_logins = {
        "user@example.com": hash_password("mypassword123"),
        "alice@panaverse.co": hash_password("secureAlicePass"),
        "bob@domain.com": hash_password("bobStrong!456")
    }

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Login failed. Incorrect email or password.")

if __name__ == "__main__":
    main()
