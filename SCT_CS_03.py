import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ Password too short (min 8 chars)")

    # Criteria 2: Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Add uppercase letters")

    # Criteria 3: Lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Add lowercase letters")

    # Criteria 4: Digits
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("❌ Add numbers")

    # Criteria 5: Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("❌ Add special characters")

    # Result
    levels = {
        1: "Very Weak 🔴",
        2: "Weak 🟠",
        3: "Moderate 🟡",
        4: "Strong 🟢",
        5: "Very Strong 🟢💪"
    }

    print(f"\nPassword Strength: {levels.get(strength, 'Invalid')}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(" -", f)


if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    check_password_strength(pwd)
