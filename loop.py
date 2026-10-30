fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(fruit)
    
for i in range(len(fruits)):
    print(fruits[i])
    
# printing odd numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    if i%2 > 0:
        print(i)
    
for num in range(1, 6):
    print(num)
    
    # Enumerate
    names = ["Alice", "Bob", "Charlie"]
    
for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")
        
# While loop
    
numbers = []
    
i = 1
    
while i <= 5:
    numbers.append(i)
    i += 1

print(numbers)

# 
even_numbers = []
num = 2

while num <= 10:
    even_numbers.append(num)
    num += 2

print(even_numbers)

