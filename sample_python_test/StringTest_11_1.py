Course = "Python for Beginner"
print(Course)
print("-- Converting in Upper Case --")
print(Course.upper())
print("-- Converting in Lower Case --")
print(Course.lower())
# String is Immutable so , Original String can't be changed
print("Original String is - ", Course)
# Finding String index
Course.find("Python")
Course.find("y")
Course.find("B")
# Printing them
print(Course.find("Python"))
print(Course.find("y"))
print(Course.find("B"))
# Replacing word in Python
print(Course.replace("for", '4'))
# Replacing Char in Python
print(Course.replace('P', 'p'))
# Verifying String Contains - Verify if "Beginner" is available in Course
print("Beginner" in Course)

