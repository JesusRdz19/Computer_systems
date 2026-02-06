# ==================================================
# Description:
# This file contains 6 problems to practice Python loops
# (for and while structures).
# ==================================================


# --------------------------------------------------
# Problem 1: Sum of integers in a range
# --------------------------------------------------
# Description:
# Calculates the sum of all integers from 1 to n
# and the sum of even numbers in the same range.
#
# Inputs:
# - n (int)
#
# Outputs:
# - Sum 1..n
# - Even sum 1..n
#
# Validations:
# - n must be integer
# - n >= 1
#
# Test cases:
# 1) Normal: n=5
# 2) Edge case: n=1
# 3) Error: n=0
# --------------------------------------------------

n = 5

try:
    n = int(n)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Multiplication table with for
# --------------------------------------------------
# Description:
# Displays the multiplication table of a base number
# from 1 up to m.
#
# Inputs:
# - base (int)
# - m (int)
#
# Outputs:
# - Multiplication table lines
#
# Validations:
# - base and m must be integers
# - m >= 1
#
# Test cases:
# 1) Normal: base=5, m=4
# 2) Edge case: base=3, m=1
# 3) Error: m=0
# --------------------------------------------------

base = 5
m = 4

try:
    base = int(base)
    m = int(m)

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# --------------------------------------------------
# Description:
# Reads numbers until a sentinel value is entered
# and calculates the average.
#
# Inputs:
# - number (float)
# - sentinel_value = -1
#
# Outputs:
# - Count
# - Average
#
# Validations:
# - Numbers must be >= 0
# - Sentinel is ignored
#
# Test cases:
# 1) Normal: 10, 20, -1
# 2) Edge case: -1
# 3) Error: text input
# --------------------------------------------------

SENTINEL_VALUE = -1
count = 0
total = 0

numbers_to_read = [10, 20, -1]  # simulated input
index = 0

while True:
    try:
        number = float(numbers_to_read[index])
        index += 1

        if number == SENTINEL_VALUE:
            break
        elif number < 0:
            print("Error: invalid input")
            continue
        else:
            total += number
            count += 1
    except (ValueError, IndexError):
        print("Error: invalid input")
        break

if count == 0:
    print("Error: no data")
else:
    print("Count:", count)
    print("Average:", total / count)


# --------------------------------------------------
# Problem 4: Password attempts with while
# --------------------------------------------------
# Description:
# Simple password validation system with limited attempts.
#
# Inputs:
# - user_password (string)
#
# Outputs:
# - Login success
# - Account locked
#
# Validations:
# - MAX_ATTEMPTS > 0
#
# Test cases:
# 1) Normal: correct password on second try
# 2) Edge case: correct on last attempt
# 3) Error: all attempts wrong
# --------------------------------------------------

CORRECT_PASSWORD = "Chuy123"
MAX_ATTEMPTS = 3
attempts = 0

password_attempts = ["123", "Chuy123"]  # simulated input
index = 0

while attempts < MAX_ATTEMPTS:
    try:
        user_password = password_attempts[index]
        index += 1
    except IndexError:
        user_password = ""

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
    else:
        attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")


# --------------------------------------------------
# Problem 5: Simple menu with while
# --------------------------------------------------
# Description:
# Displays a menu until the user chooses to exit.
#
# Inputs:
# - option (int)
#
# Outputs:
# - Menu messages
#
# Validations:
# - Option must be 0, 1, 2 or 3
#
# Test cases:
# 1) Normal: 1, 3, 0
# 2) Edge case: 2, 0
# 3) Error: invalid option
# --------------------------------------------------

counter = 0
options = [1, 3, 2, 0]  # simulated input
index = 0
option = -1

while option != 0:
    try:
        option = int(options[index])
        index += 1
    except (ValueError, IndexError):
        print("Error: invalid option")
        continue

    if option == 1:
        print("Holi!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    elif option == 0:
        print("Chao!")
    else:
        print("Error: invalid option")


# --------------------------------------------------
# Problem 6: Pattern printing with nested loops
# --------------------------------------------------
# Description:
# Prints a right triangle pattern using asterisks.
#
# Inputs:
# - n (int)
#
# Outputs:
# - Star pattern
#
# Validations:
# - n >= 1
#
# Test cases:
# 1) Normal: n=4
# 2) Edge case: n=1
# 3) Error: n=0
# --------------------------------------------------

n = 4

try:
    n = int(n)
    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)
except ValueError:
    print("Error: invalid input")
