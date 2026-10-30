# tuples
fruits = ("apple", "banana", "cherry")
print(fruits)
# tuple concatenation
more_fruits = ("date", "elderberry")
all_fruits = fruits + more_fruits
print(all_fruits)

# tuple Slicing
numbers = (1, 2, 3, 4, 5)
sliced_numbers = numbers[1:4]
print(sliced_numbers)

# nested tuples
nested_tuple = (("apple", "banana"), (10, 20, 30), ("x", "y", "z"))
print(nested_tuple[1])  
print(nested_tuple[0][1]) # accessing banana
print(nested_tuple[1][0:2]) # access first two elements of the second tupple

# list
fruits_list = ["apple", "banana", "cherry", "date", "elderberry"]
forward_slice = fruits_list[1:3]
print(forward_slice)

bakward_slice = fruits_list[-3:-1]
print(bakward_slice)

# list striding

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
strided_numbers = numbers[0:9:2]
print(strided_numbers)

# nested lists
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(nested_list[2])

# list add/ remove

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

numbers.remove(3)
print(numbers)