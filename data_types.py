age = 25
temperature = -10
population = 780000000
pi = 3.14159
price = 19.99
scientific_notation = 1.5e3
name = "John Doe"
greeting = 'Hello, World!'
is_valid = True
comparison = 10 > 5
empty_check = bool("")
num_float = float(age)
pi_int = int(pi)

print(type(age))
print(type(temperature))
print(type(population))
print(type(pi))
print(type(price))
print(type(scientific_notation))    
print(type(name))
print(type(greeting))
print(type(is_valid))
print(type(comparison))
print(type(empty_check))
print(type(num_float))
print(type(pi_int))

print(name[-5])

sliced_name = name[0:6]
print(sliced_name)

# Striding is used to skip characters while slicing

strided = greeting[0:10:2]
print(strided)

my_string = "I love python programming"
replaced =  my_string.replace("python", "Java")
print(replaced)