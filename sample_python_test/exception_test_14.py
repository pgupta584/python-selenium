# PART - I
# Try catch - Else
a = 20

# Understanding try-catch-else while using exception --> use based on requirement
def test_exception_14(number):
    print("Start Exception code")
    try:
        divide = a / number
        print(divide)
        print("Test Precondition Done")
    except ZeroDivisionError:
        print("We cannot divide by zero")
    else:
        print("Else Block Executed - Since there is no Exception")
        print("Test executed as Precondition is pass")


print("Function call started")
test_exception_14(1)
print("Function call Ended")

print("Function call started")
test_exception_14(0)
print("Function call Ended")

