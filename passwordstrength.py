import re

def check_password_strength(password):
    # Criteria for password strength
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r"[A-Z]", password) is not None,
        "lowercase": re.search(r"[a-z]", password) is not None,
        "digit": re.search(r"\d", password) is not None,
        "special_char": re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    }

    # Assessing strength based on criteria
    strength_score = sum(criteria.values())
    feedback = []

    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Password should include at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Password should include at least one lowercase letter.")
    if not criteria["digit"]:
        feedback.append("Password should include at least one digit.")
    if not criteria["special_char"]:
        feedback.append("Password should include at least one special character.")

    # Determine the strength of the password
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# Example usage
password = input("Enter a password to check its strength: ")
strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for suggestion in feedback:
        print(f"- {suggestion}")
