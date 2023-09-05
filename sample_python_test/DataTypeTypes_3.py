a = 10
b = 10.5
c = "Hello"
d = 'Pankaj'
e = 10 + 5j
# Let's print it's type
print("Data type for a is --> ", type(a))
print("Data type for b is --> ", type(b))
print("Data type for c is --> ", type(c))
print("Data type for d is --> ", type(d))
print("Data type for e is --> ", type(e))

# List
list_object = [1, 1.5, "Hello"]
print("List is --> ", list_object)
list_object[0] = 5
print("List is --> ", list_object)

# Tuple
tuple_object = (2, 2.5, "World")
print("List is --> ", tuple_object)
# tuple_object[0] = 10 -- Tuple doesn't support assignment operator
# print("List is --> ", tuple_object)

# Dictionary
dictionary_object = {"Name": "Pankaj", 2: "Gupta", 3: 50}  # We can keep key-value whatever we want
print("dictionary is --> ", dictionary_object)
# Printing values
print("Printing value of key Name --> ", dictionary_object["Name"])
