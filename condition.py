x = 10
if x > 5:
    print("x is greater than 5")
    
a = 10
b = 20
print(a == b)
print(a < b)

age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
number = 7
if number % 2 == 1:
    print("The number is odd.")
    
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")   
else:
    print("Grade: C")
    
    
age = 25
income = 50000
if age > 18 and income > 30000:
    print("You are eligible for the loan.")

else:
    print("You are not eligible for the loan.")
    
    
# leap year check

year = 2099

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")