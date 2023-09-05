# Function is group of related statements that use to achieve some goal OR perform some specific task
# Take one example

# Example 1 - Basic
def get_name():  # Create function using def fn():
    print("My Name is --> Pankaj")


# Example 2 - Function with Parameter
def get_name_dynamic(name):  # Function with Parameter
    print("My Name is --> ", name)


# Example 3 - Function with return
def get_number_sum(a, b):  # Function with Return
    addition = a + b
    print("Sum is --> ", addition)
    return addition


# Code indentation is very important here

# Calling function
get_name()
get_name_dynamic("Gupta")
get_number_sum(5, 2)
