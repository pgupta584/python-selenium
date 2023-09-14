# PART - I
# Try catch - Else
a = 20


# Understanding try-catch-else while using exception --> use based on requirement
def test_exception_15(number):
    print("Start Exception code")
    try:
        divide = a / number
        print(divide)
        print("Test Precondition Done")
    except ZeroDivisionError:
        print("We cannot divide by zero")
    else:
        print("Else Block Executed - Since there is no Exception")
    finally:
        print("Finally Block Executed - Always")


# Some Python Version else & finally can't be used together, hence use accordingly - My python is 3.8
print("Function call started")
test_exception_15(1)
print("Function call Ended")

print("Function call started")
test_exception_15(0)
print("Function call Ended")


# Part - II
# When we want a piece of code to be executed irrespective of exception then use those line of code in finally block
# def test_db_connection_15(number):
#     try:
#         print("Start DB")
#         divide = a / number
#         print(divide)
#         print("Test Precondition Done")
#     except ZeroDivisionError:
#         print("We cannot divide by zero")
#     finally:
#         print("Close Db Connection")
#
#
# print("Function call started")
# test_exception_15(0)
# print("Function call Ended")
