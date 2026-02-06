# ==================================================
# Purpose:
# Practice string manipulation in Python: creation,
# normalization, indexing, slicing, searching,
# replacing, splitting, joining and formatting text.
# ==================================================


# --------------------------------------------------
# Problem 1: Full name formatter (name + initials)
# --------------------------------------------------
# Description:
# Formats a full name into Title Case and generates
# the initials from each word.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - Formatted name
# - Initials
#
# Validation:
# - Not empty after strip()
# - At least two words
#
# Test cases:
# 1) Normal: "jesus rodriguez"
# 2) Edge case: " Daniel Ruiz "
# 3) Error: "   "
# --------------------------------------------------

full_name = "jesus rodriguez".strip()

if full_name == "":
    print("Error: invalid input")
else:
    name_parts = full_name.split()

    if len(name_parts) < 2:
        print("Error: invalid input")
    else:
        formatted_name = full_name.title()
        initials = ""

        for part in name_parts:
            initials += part[0].upper() + "."

        print("Formatted name:", formatted_name)
        print("Initials:", initials)


# --------------------------------------------------
# Problem 2: Simple email validator (structure + domain)
# --------------------------------------------------
# Description:
# Validates a basic email structure and extracts
# the domain if valid.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - Valid email
# - Domain (if valid)
#
# Validation:
# - Not empty
# - Exactly one '@'
# - Contains '.' after '@'
# - No spaces
#
# Test cases:
# 1) Normal: "jesusrodriguez11@gmail.com"
# 2) Edge case: "rodriguezjesus@gmail.com"
# 3) Error: "jesus rodriguez@gmail.com"
# --------------------------------------------------

email_text = "jesusrodriguez11@gmail.com".strip()

if email_text == "":
    print("Error: invalid input")
else:
    if " " in email_text or email_text.count("@") != 1:
        print("Valid email: False")
    else:
        at_index = email_text.find("@")
        domain_part = email_text[at_index + 1:]

        if "." not in domain_part:
            print("Valid email: False")
        else:
            print("Valid email: True")
            print("Domain:", domain_part)


# --------------------------------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# --------------------------------------------------
# Description:
# Checks if a phrase is a palindrome ignoring
# spaces and letter case.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - Is palindrome
#
# Validation:
# - Not empty after strip()
# - Minimum length after cleaning
#
# Test cases:
# 1) Normal: "Anita lava la tina"
# 2) Edge case: "oso"
# 3) Error: "  "
# --------------------------------------------------

phrase = "Anita lava la tina".strip()

if phrase == "":
    print("Error: invalid input")
else:
    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < 3:
        print("Error: invalid input")
    else:
        is_palindrome = normalized_phrase == normalized_phrase[::-1]
        print("Is palindrome:", is_palindrome)


# --------------------------------------------------
# Problem 4: Sentence word statistics
# --------------------------------------------------
# Description:
# Analyzes a sentence to extract word statistics.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Word count
# - First word
# - Last word
# - Shortest word
# - Longest word
#
# Validation:
# - Not empty after strip()
#
# Test cases:
# 1) Normal: "Jesus Rodriguez studies engineering"
# 2) Edge case: "Daniel"
# 3) Error: ""
# --------------------------------------------------

sentence = "Jesus Rodriguez studies engineering".strip()

if sentence == "":
    print("Error: invalid input")
else:
    words = sentence.split()

    if len(words) == 0:
        print("Error: invalid input")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]

        shortest_word = words[0]
        longest_word = words[0]

        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word
            if len(word) > len(longest_word):
                longest_word = word

        print("Word count:", word_count)
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Shortest word:", shortest_word)
        print("Longest word:", longest_word)


# --------------------------------------------------
# Problem 5: Password strength classifier
# --------------------------------------------------
# Description:
# Classifies a password as weak, medium or strong
# based on length and character variety.
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - Password strength
#
# Validation:
# - Not empty
#
# Test cases:
# 1) Normal: "Jesus123!"
# 2) Edge case: "jesus2024"
# 3) Error: ""
# --------------------------------------------------

password_input = "Jesus123!".strip()

if password_input == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    length_ok = len(password_input) >= 8

    if length_ok and has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif length_ok and (has_upper or has_digit):
        strength = "medium"
    else:
        strength = "weak"

    print("Password strength:", strength)


# --------------------------------------------------
# Problem 6: Product label formatter (fixed-width text)
# --------------------------------------------------
# Description:
# Generates a fixed-width product label of exactly
# 30 characters.
#
# Inputs:
# - product_name (string)
# - price_value (number)
#
# Outputs:
# - Label
#
# Validation:
# - product_name not empty
# - price_value positive
#
# Test cases:
# 1) Normal: "Laptop", 15999.99
# 2) Edge case: very long product name
# 3) Error: negative price
# --------------------------------------------------

product_name = "Laptop".strip()
price_value_text = "15999.99"

try:
    price_value = float(price_value_text)

    if product_name == "" or price_value <= 0:
        print("Error: invalid input")
    else:
        label = f"Product: {product_name} | Price: ${price_value}"

        if len(label) > 30:
            label = label[:30]
        else:
            label = label + " " * (30 - len(label))

        print(f'Label: "{label}"')

except ValueError:
    print("Error: invalid input")
