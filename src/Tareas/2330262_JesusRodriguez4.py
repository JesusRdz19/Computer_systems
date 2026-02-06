# ==================================================
# Purpose:
# Practice numeric types (int, float) and boolean values
# using arithmetic operations, comparisons, logical
# evaluations, casting, rounding, and simple decisions.
# ==================================================


# --------------------------------------------------
# Problem 1: Temperature converter and range flag
# --------------------------------------------------
# Description:
# Converts a temperature from Celsius to Fahrenheit
# and Kelvin, and determines if it is a high temperature.
#
# Inputs:
# - temp_c (float)
#
# Outputs:
# - Fahrenheit
# - Kelvin
# - High temperature
#
# Validations:
# - temp_c must be convertible to float
# - temp_c >= -273.15
#
# Test cases:
# 1) Normal: temp_c = 32.0
# 2) Edge case: temp_c = -273.15
# 3) Error: temp_c = "abc"
# --------------------------------------------------

temp_c_text = "32.0"

try:
    temp_c = float(temp_c_text)

    if temp_c < -273.15:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)

except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Work hours and overtime payment
# --------------------------------------------------
# Description:
# Calculates weekly payment including overtime pay.
#
# Inputs:
# - hours_worked (int)
# - hourly_rate (float)
#
# Outputs:
# - Regular pay
# - Overtime pay
# - Total pay
# - Has overtime
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
#
# Test cases:
# 1) Normal: 45 hours, rate 100.0
# 2) Edge case: 40 hours
# 3) Error: hours_worked = -5
# --------------------------------------------------

hours_worked_text = "45"
hourly_rate_text = "100.0"

try:
    hours_worked = int(hours_worked_text)
    hourly_rate = float(hourly_rate_text)

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", has_overtime)

except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: Discount eligibility with booleans
# --------------------------------------------------
# Description:
# Determines if a customer is eligible for a discount
# and calculates the final total.
#
# Inputs:
# - purchase_total (float)
# - is_student_text (string)
# - is_senior_text (string)
#
# Outputs:
# - Discount eligible
# - Final total
#
# Validations:
# - purchase_total >= 0.0
# - Text must be YES or NO
#
# Test cases:
# 1) Normal: 1200.0, YES, NO
# 2) Edge case: 1000.0, NO, NO
# 3) Error: student_text = "MAYBE"
# --------------------------------------------------

purchase_total_text = "1200.0"
is_student_text = "YES"
is_senior_text = "NO"

try:
    purchase_total = float(purchase_total_text)
    is_student_text = is_student_text.strip().upper()
    is_senior_text = is_senior_text.strip().upper()

    if purchase_total < 0.0:
        print("Error: invalid input")
    elif is_student_text not in ["YES", "NO"] or is_senior_text not in ["YES", "NO"]:
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = is_student or is_senior or purchase_total >= 1000.0

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", discount_eligible)
        print("Final total:", final_total)

except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 4: Basic statistics of three integers
# --------------------------------------------------
# Description:
# Calculates sum, average, max, min and checks
# if all numbers are even.
#
# Inputs:
# - n1, n2, n3 (int)
#
# Outputs:
# - Sum
# - Average
# - Max
# - Min
# - All even
#
# Validations:
# - Values must be convertible to int
#
# Test cases:
# 1) Normal: 2, 4, 6
# 2) Edge case: 0, 1, 2
# 3) Error: n1 = "abc"
# --------------------------------------------------

n1_text = "2"
n2_text = "4"
n3_text = "6"

try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)

except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 5: Loan eligibility (income and debt ratio)
# --------------------------------------------------
# Description:
# Determines loan eligibility based on income,
# debt ratio and credit score.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - Debt ratio
# - Eligible
#
# Validations:
# - monthly_income > 0
# - monthly_debt >= 0
# - credit_score >= 0
#
# Test cases:
# 1) Normal: 10000, 3000, 700
# 2) Edge case: income = 8000
# 3) Error: income = 0
# --------------------------------------------------

monthly_income_text = "10000"
monthly_debt_text = "3000"
credit_score_text = "700"

try:
    monthly_income = float(monthly_income_text)
    monthly_debt = float(monthly_debt_text)
    credit_score = int(credit_score_text)

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print("Debt ratio:", debt_ratio)
        print("Eligible:", eligible)

except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 6: Body Mass Index (BMI) and category flag
# --------------------------------------------------
# Description:
# Calculates BMI and determines weight category.
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - BMI
# - Underweight
# - Normal
# - Overweight
#
# Validations:
# - weight_kg > 0
# - height_m > 0
#
# Test cases:
# 1) Normal: 70 kg, 1.75 m
# 2) Edge case: bmi = 18.5
# 3) Error: height_m = 0
# --------------------------------------------------

weight_kg_text = "70"
height_m_text = "1.75"

try:
    weight_kg = float(weight_kg_text)
    height_m = float(height_m_text)

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)

        is_underweight = bmi < 18.5
        is_normal = bmi >= 18.5 and bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", bmi_rounded)
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)

except ValueError:
    print("Error: invalid input")
