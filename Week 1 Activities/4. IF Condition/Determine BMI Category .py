# Function to calculate BMI and determine the category
def determine_bmi_category(height, weight):
    bmi = weight / (height ** 2)
    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi_category = determine_bmi_category(height, weight)
print(f"BMI Category: {bmi_category}")
