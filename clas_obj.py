print("Class and Object Example")

class Car:
    
    brand = "Toyota"
    wheels = 4
    
    
    def start_engine(self):
        return "Engine started"
    
# object

my_car = Car()

print(my_car.brand)

print(my_car.start_engine())


# class ClassName:
#  attributes1 = value1
#  attributes2 = value2

# def __init_(self, parameters):
#  self.attribute1 = parameter1

# def method_name(self):


class Calculator:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
calc = Calculator(10, 5)

print(calc.add())  # Output: 15

# Begin by defining a function named calculate_percentage with two parameters: a and b. 
# This function will calculate the percentage based on the given values of a and b.

# Inside the function, write the calculation logic. 
# The formula for calculating the percentage is (a / b) * 100. 
# So, return the result of this calculation.

# After defining the function, outside the function block, assign the value 234 to the variable a and 5607 to the variable b. 
# These are the values for which you want to calculate the percentage.

# Now, call the calculate_percentage function with the variables a and b as arguments. 
# Assign the returned result to a variable named result.

# Finally, print the result using the print() function. Include a string "Percentage:" 
# followed by the variable result.

def calculate_percentage(a, b):
    return (a / b) * 100
a = 234
b = 5607
 
result = calculate_percentage(a, b)
print("Percentage:", result)