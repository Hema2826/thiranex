import re

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty",
    "admin", "welcome", "password123"
}

def analyze_password(password):
    score = 0
    feedback = []

    # Length
    length = len(password)
    if length >= 16:
        score += 30
    elif length >= 12:
        score += 25
    elif length >= 8:
        score += 15
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Character variety
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        feedback.append("Add special characters.")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = max(score - 30, 0)
        feedback.append("This is a commonly used password.")

    # Determine strength
    if score >= 76:
        strength = "Strong"
    elif score >= 51:
        strength = "Good"
    elif score >= 26:
        strength = "Fair"
    else:
        strength = "Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

if __name__ == "__main__":
    pwd = input("Enter password: ")
    result = analyze_password(pwd)

    print("\nPassword Analysis")
    print("-----------------")
    print("Score:", result["score"])
    print("Strength:", result["strength"])

    if result["feedback"]:
        print("\nSuggestions:")
        for item in result["feedback"]:
            print("-", item)