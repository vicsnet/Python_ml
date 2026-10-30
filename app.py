age = 25
price = 19.95
first_name = "Vincent"
is_online = True

name = input("What is your name? ")


print(age)
print("Hello " + name)

birth_year =  input("Enter your birth year: ")


age = 2025 - int(birth_year)

print(age)

print("Calculator")
first = input("First: ")
second = input("Second: ")
sum = int(first) + int(second)
print("Sum: " + str(sum))

course = "Python for Beginners"
course.upper()
print(course)
print(course.replace('for', '4'))
# in operator
print('Python' in course)

# logical operators
# and
# or
# not

price = 25
print(price > 10 and price < 30)

# if statements
temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
    
print("Done")

# weight converter
weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = int(weight) / 0.45
    print("Weight in Lbs: " + str(converted))
    
else:
    converted = int(weight) * 0.45
    print("Weight in Kgs: " + str(converted))
    
# while loop
i = 1
while i <= 5:
    print(i)
    print(i * '*')
    i = i + 1
    
print("Done")

# lists

names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[0])
names[0] = "Jon"
print(names[0])

numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)
print(numbers)
numbers.remove(3)

print(1 in numbers)
numbers.clear()
print(numbers)

