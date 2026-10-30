def greet(name):
    print(f"Hello, {name}!")
    
greet("Alice")

def function_name(parameters):
    
    """
    Function body
    """
    result = parameters * 2  # Example operation
    # Function body
    return result

a = function_name(5)  # Example function call
print(a)

# temp
def process_temperature(temp):
    if temp < -273.15:
        return "Invalid temperature! Below absolute zero."
    elif temp > 100:
        return "Temperature exceeds boiling point!"
    else:
        return f"Temperature in Fahrenheit: {temp * 9/5 + 32}"
    
print(process_temperature(-300))  # Invalid temperature
print(process_temperature(25))    # Valid temperature


# Global vaariable
global_variable = "I am a global variable"

counter = 0

def increment_counter():
    global counter  # Declare counter as global to modify it
    counter += 1
    print(f"Counter value: {counter}")

def reset():
    global counter
    counter = 0
    print("Counter reset to 0.")
    
    
increment_counter()  # Call the function to increment the counter
increment_counter()  # Call the function again to see the updated value
reset()  # Reset the counter

increment_counter()  # Call the function after reset to see the updated value


# local variable

def calculate_area(radius):
    pi = 3.14159  # Local variable
    area = pi * radius ** 2
    return area

print(calculate_area(5))  # Call the function with a radius of 5

# A bank want to calculate the compound interest for its customers based on their principal
# amount, annual interest rate, and the number of years the money is invested. The formula for compound interest is:

# A = P * (1 + r/n)^(n*t)

# Where:
# A = final amount(principal + interest)
# P = principal amount
# r = annual interest rate (in decimal form)
# n = number of times interest is compounded per year
# t = time in years


def calculate_compound_interest(p, r, n, t):

    
    final_amount = p * (1 + r/n) ** (n*t)
    return final_amount

calculated_amount = calculate_compound_interest(1000, 0.05, 5, 12)  
print(f"Final amount after compound interest: {calculated_amount:.2f}")

# A health organization needs a program to calculate a person's  body mass index and provide an assessment based on the result.
# The BMI is calculated using the formula:
#  BMI = Weight(kg) / height(m)^2

# The function should also classify the BMI into the following categories:
# underweight: BMI < 18.5
# normal weight: 18.5 <= BMI < 25
# overweight: 25 <= BMI < 30
# obese: BMI >= 30

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        assessment = "Underweight"
    elif 18.5 <= bmi < 25:
        assessment = "Normal weight"
    elif 25 <= bmi < 30:
        assessment = "Overweight"
    else:
        assessment = "Obese"
    
    return bmi, assessment

print(calculate_bmi(90, 1.75))  # Example usage with weight in kg and height in meters
