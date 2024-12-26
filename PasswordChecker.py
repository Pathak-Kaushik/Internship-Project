import re

def assess_password_strength(password):
    """
    Evaluate the strength of a given password.

    Args:
        password (str): The password to evaluate.

    Returns:
        dict: A dictionary with password assessment details.
    """
    criteria = {
        'has_min_length': len(password) >= 8,
        'contains_uppercase': bool(re.search(r"[A-Z]", password)),
        'contains_lowercase': bool(re.search(r"[a-z]", password)),
        'contains_digit': bool(re.search(r"\d", password)),
        'contains_special_char': bool(re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password))
    }

    # Calculate the strength score
    score = sum(criteria.values())

    # Define strength levels
    strength_labels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    strength_level = strength_labels[score]

    return {
        'criteria': criteria,
        'score': score,
        'strength_label': strength_level
    }

# Demonstration
if __name__ == "__main__":
    user_password = input("Enter a password: ")
    evaluation = assess_password_strength(user_password)

    print("\nPassword Evaluation Results:")
    print("-----------------------------")
    for criterion, met in evaluation['criteria'].items():
        print(f"{criterion.replace('_', ' ').capitalize()}: {'Yes' if met else 'No'}")

    print(f"\nOverall Score: {evaluation['score']}/5")
    print(f"Strength Level: {evaluation['strength_label']}")
