# ==================================================
# Description:
# This file contains 6 problems to practice Python collections
# (lists, tuples and dictionaries).
# ==================================================


# --------------------------------------------------
# Problem 1: Shopping list basics
# --------------------------------------------------
# Description:
# Works with a shopping list of products and quantities.
#
# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)
#
# Outputs:
# - Items list
# - Total items
# - Found item
#
# Validations:
# - Input text not empty
# - Items normalized to lowercase
#
# Test cases:
# 1) Normal: "apple:2,banana:5", new_item="milk"
# 2) Edge case: one initial item
# 3) Error: empty initial text
# --------------------------------------------------

initial_items_text = "apple:2,banana:5,orange:6"
new_item = "Milk"
search_item = "banana"

if initial_items_text.strip() == "" or new_item.strip() == "" or search_item.strip() == "":
    print("Error: invalid input")
else:
    items_list = []

    for item in initial_items_text.split(","):
        items_list.append(item.strip().lower())

    items_list.append(new_item.strip().lower())

    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", search_item.strip().lower() in items_list)


# --------------------------------------------------
# Problem 2: Points and distances with tuples
# --------------------------------------------------
# Description:
# Calculates distance and midpoint between two points.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - Point A
# - Point B
# - Distance
# - Midpoint
#
# Validations:
# - Values convertible to float
#
# Test cases:
# 1) Normal: (0,0) and (4,3)
# 2) Edge case: same points
# 3) Error: invalid value
# --------------------------------------------------

try:
    x1, y1 = 0.0, 0.0
    x2, y2 = 4.0, 3.0

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: Product catalog with dictionary
# --------------------------------------------------
# Description:
# Calculates total price for a product using a dictionary.
#
# Inputs:
# - product_name (string)
# - quantity (int)
#
# Outputs:
# - Unit price
# - Quantity
# - Total
#
# Validations:
# - Product exists
# - Quantity > 0
#
# Test cases:
# 1) Normal: apple, 3
# 2) Edge case: quantity=1
# 3) Error: product not found
# --------------------------------------------------

product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0
}

product_name = "Apple"
quantity = 3

if product_name.strip() == "" or quantity <= 0:
    print("Error: invalid input")
else:
    product_name = product_name.strip().lower()

    if product_name in product_prices:
        unit_price = product_prices[product_name]
        total = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total)
    else:
        print("Error: product not found")


# --------------------------------------------------
# Problem 4: Student grades with dict and list
# --------------------------------------------------
# Description:
# Calculates average grade and pass status for a student.
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - Grades
# - Average
# - Passed
#
# Validations:
# - Student exists
# - Grades list not empty
#
# Test cases:
# 1) Normal: Chuy
# 2) Edge case: one grade
# 3) Error: student not found
# --------------------------------------------------

student_grades = {
    "chuy": [80, 90, 85],
    "charly": [70, 75, 72],
    "dan": [60, 65, 68]
}

student_name = "Chuy"

if student_name.strip() == "":
    print("Error: invalid input")
else:
    student_name = student_name.strip().lower()

    if student_name in student_grades:
        grades_list = student_grades[student_name]

        if len(grades_list) == 0:
            print("Error: invalid input")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = average >= 70
            print("Grades:", grades_list)
            print("Average:", average)
            print("Passed:", is_passed)
    else:
        print("Error: student not found")


# --------------------------------------------------
# Problem 5: Word frequency counter
# --------------------------------------------------
# Description:
# Counts word frequency in a sentence.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Words list
# - Frequencies
# - Most common word
#
# Validations:
# - Sentence not empty
#
# Test cases:
# 1) Normal: "Chuy likes python and chuy likes code"
# 2) Edge case: one word
# 3) Error: empty string
# --------------------------------------------------

sentence = "Chuy likes python, and Chuy likes code!"

if sentence.strip() == "":
    print("Error: invalid input")
else:
    clean_sentence = sentence.lower()
    for ch in [".", ",", "!", "?", ";", ":"]:
        clean_sentence = clean_sentence.replace(ch, "")

    words_list = clean_sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        most_common_word = ""
        max_count = 0

        for word, count in freq_dict.items():
            if count > max_count:
                max_count = count
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


# --------------------------------------------------
# Problem 6: Simple address book
# --------------------------------------------------
# Description:
# Simple address book with add, search and delete actions.
#
# Inputs:
# - action_text (string)
# - name (string)
# - phone (string)
#
# Outputs:
# - Operation result messages
#
# Validations:
# - Valid action
# - Name not empty
#
# Test cases:
# 1) Normal: ADD Chuy 12345
# 2) Edge case: SEARCH Charly
# 3) Error: DELETE Victor (not found)
# --------------------------------------------------

contacts = {
    "Chuy": "111111",
    "Charly": "222222",
    "Dan": "333333"
}

action_text = "ADD"
name = "Victor"
phone = "444444"

action_text = action_text.strip().upper()
name = name.strip().title()

if action_text not in ["ADD", "SEARCH", "DELETE"] or name == "":
    print("Error: invalid input")
else:
    if action_text == "ADD":
        if phone.strip() == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone.strip()
            print("Contact saved:", name, phone)

    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")
