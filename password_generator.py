import random
import string

def generate_secure_password(length):
    """Generates a cryptographically strong password based on security protocols."""
    
    # Security Check: Minimum password length must be 4 to include all character types
    if length < 4:
        return "❌ Error: For strict security, password length must be at least 4."

    # Step 1: Define character sets for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    symbols = string.punctuation

    # Step 2: Ensure at least one character from each category is included
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(nums),
        random.choice(symbols)
    ]

    # Step 3: Fill the remaining length with random choices from all available characters
    all_chars = lower + upper + nums + symbols
    password += random.choices(all_chars, k=length - 4)

    # Step 4: Shuffle the list to prevent any predictable sequence or pattern
    random.shuffle(password)

    # Step 5: Convert the list back into a single string
    return "".join(password)

if __name__ == "__main__":
    print("--- 🔐 Secure Password Generator ---")
    try:
        user_length = int(input("Enter desired password length (e.g., 8, 12, 16): "))
        final_password = generate_secure_password(user_length)
        print(f"\n✅ Generated Password: {final_password}")
        print("-" * 45)
    except ValueError:
        print("\n❌ Invalid Input! Please enter a valid numerical value.")
