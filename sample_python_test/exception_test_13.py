# Python code to show how to raise an exception in Python
num = [3, 4, 5, 7]
a = 10
b = 0


# PART - I
# if len(num) > 3:
#     print("Start Exception code")
#     raise Exception(f"Length of the given list must be less than or equal to 3 but is {len(num)}")

# PART - II
# def test_exception():
#     print("Start Exception code")
#     divide = a/b
#     print(divide)

# PART - III
def test_exception(number):
    print("Start Exception code")
    try:
        divide = a / number
        print(divide)
    except ZeroDivisionError:
        print("We cannot divide by zero")


# PART - III
test_exception(1)
# Run this test as Python Test
# /Users/pankaj.gup/Documents/MYGIT/Pyhon-Selenium/python-selenium/sample_python_test/exception_test_13.py
# Output ----
# Start Exception code
# 10
print("Exception case --")
test_exception(0)
print("Exceptions are handled")
# Run this test as Python Test
# /Users/pankaj.gup/Documents/MYGIT/Pyhon-Selenium/python-selenium/sample_python_test/exception_test_13.py
# Output ---- Normal execution without termination

