# set are unordered
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)
my_set.update([7, 8, 9])
print("Updated Set:", my_set)

my_set.remove(3)
print("Set after removing 3:", my_set)

my_set.discard(10)  # discard does not raise an error if the element is not found
print("Set after discarding 10:", my_set)

my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
my_set_from_list = set(my_list)
print("Set:", my_set_from_list)

# set union
set_a = {1, 2, 3, 4}
print("Set A:", set_a)
set_b = {3, 4, 5}
print("Set B:", set_b)
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# set intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

set3 = {1, 2, 3, 4}
set4 = {4, 5, 6, 7}

result = set3 - set4

print(result)