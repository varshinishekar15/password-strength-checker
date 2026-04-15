def check_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if any(char.islower() for char in password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        remarks.append("Add at least one number.")

    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(char in special_characters for char in password):
        score += 1
    else:
        remarks.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, remarks


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")

    strength, remarks = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    if remarks:
        print("\nSuggestions to improve your password:")
        for remark in remarks:
            print(f"- {remark}")
    else:
        print("Your password is well structured.")


if __name__ == "__main__":
    main()
