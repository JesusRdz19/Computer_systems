# ==================================================
# Description:
# This file contains 6  problems to practice Python functions
# ==================================================


# --------------------------------------------------
# Problem 1: Rectangle area and perimeter
# --------------------------------------------------
# Description:
# Calculates the area and perimeter of a rectangle
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - Area
# - Perimeter
#
# Conditions:
# - width > 0
# - height > 0
#
# Test cases:
# 1) Normal: width=5, height=3
# 2) Edge case: width=0.1, height=0.1
# 3) Error: width=-2, height=4
# --------------------------------------------------

def calculate_area(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


width = 5
height = 3

if width > 0 and height > 0:
    print("Area:", calculate_area(width, height))
    print("Perimeter:", calculate_perimeter(width, height))
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Grade classifier
# --------------------------------------------------
# Description:
# Classifies a numeric score into a letter grade.
#
# Inputs:
# - score (int or float)
#
# Outputs:
# - Score
# - Category
#
# Conditions:
# - 0 <= score <= 100
#
# Test cases:
# 1) Normal: score=85
# 2) Edge case: score=100
# 3) Error: score=120
# --------------------------------------------------

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


score = 85

if 0 <= score <= 100:
    print("Score:", score)
    print("Category:", classify_grade(score))
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: List statistics
# --------------------------------------------------
# Description:
# Receives a list of numbers and returns min, max,
# and average.
#
# Inputs:
# - numbers_text (string)
#
# Outputs:
# - Min
# - Max
# - Average
#
# Conditions:
# - Input text not empty
# - List not empty
# - All values numeric
#
# Test cases:
# 1) Normal: "10,20,30"
# 2) Edge case: "5"
# 3) Error: "10,a,30"
# --------------------------------------------------

def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }


numbers_text = "10,20,30"

if numbers_text.strip() == "":
    print("Error: invalid input")
else:
    try:
        numbers_list = []
        for item in numbers_text.split(","):
            numbers_list.append(float(item.strip()))

        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            summary = summarize_numbers(numbers_list)
            print("Min:", summary["min"])
            print("Max:", summary["max"])
            print("Average:", summary["average"])
    except ValueError:
        print("Error: invalid input")


# --------------------------------------------------
# Problem 4: Apply discount list
# --------------------------------------------------
# Description:
# Applies a discount to a list of prices without
# modifying the original list.
#
# Inputs:
# - prices_text (string)
# - discount_rate (float)
#
# Outputs:
# - Original prices
# - Discounted prices
#
# Conditions:
# - Prices > 0
# - 0 <= discount_rate <= 1
#
# Test cases:
# 1) Normal: "100,200,300", 0.10
# 2) Edge case: "50", 0
# 3) Error: "100,-20", 0.10
# --------------------------------------------------

def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        discounted.append(price * (1 - discount_rate))
    return discounted


prices_text = "100,200,300"
discount_rate = 0.10

if prices_text.strip() == "" or not (0 <= discount_rate <= 1):
    print("Error: invalid input")
else:
    try:
        prices_list = []
        for item in prices_text.split(","):
            price = float(item.strip())
            if price <= 0:
                raise ValueError
            prices_list.append(price)

        discounted_prices = apply_discount(prices_list, discount_rate)
        print("Original prices:", prices_list)
        print("Discounted prices:", discounted_prices)
    except ValueError:
        print("Error: invalid input")


# --------------------------------------------------
# Problem 5: Greeting function 
# --------------------------------------------------
# Description:
# Generates a greeting message .
#
# Inputs:
# - name (string)
# - title (string, optional)
#
# Outputs:
# - Greeting
#
# Conditions:
# - Name not empty
#
# Test cases:
# 1) Normal: name="Chuy", title="Ing."
# 2) Edge case: name="Charly", title=""
# 3) Error: name=""
# --------------------------------------------------

def greet(name, title=""):
    if title.strip() != "":
        full_name = f"{title.strip()} {name.strip()}"
    else:
        full_name = name.strip()
    return f"Hello, {full_name}!"


name = "Chuy"
title = "Ing."

if name.strip() == "":
    print("Error: invalid input")
else:
    greeting_message = greet(name=name, title=title)
    print("Greeting:", greeting_message)


# --------------------------------------------------
# Problem 6: Factorial function
# --------------------------------------------------
# Description:
# Calculates the factorial of a number using
# an iterative approach.
#
# Inputs:
# - n (int)
#
# Outputs:
# - n
# - Factorial
#
# Conditions:
# - n is integer
# - n >= 0
# - n <= 20
#
# Test cases:
# 1) Normal: n=5
# 2) Edge case: n=0
# 3) Error: n=-3
# --------------------------------------------------

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = 5

if isinstance(n, int) and 0 <= n <= 20:
    print("n:", n)
    print("Factorial:", factorial(n))
else:
    print("Error: invalid input")
