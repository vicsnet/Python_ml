# Dictionaries
## A dictionary is an unordered, mutable and indexed collection of key-value pairs in python
student = {"name": "John", "age": 20, "grade": "A"}
print(student)

profile = {"name": "Alice", "age": 25, "city": "New York"}

name = profile["name"]

print("Name:", name)

age = profile["age"]
print("Age:", age)

profile["email"] = "alice@example.com"
print("Profile:", profile)

keys = profile.keys()
print("Keys:", keys)

values = profile.values()
print("Values:", values)

items = profile.items()
print("Items:", items)  