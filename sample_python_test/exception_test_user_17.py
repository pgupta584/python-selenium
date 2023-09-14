from sample_python_test.exception_test_user_16 import WrongDivisionException

a = 20
# Testing exception - we can use previous example & test - Test_15

class TestException:
    @staticmethod
    def test_exception_17(number):
        print("Start Exception code")
        try:
            divide = a / number
            print(divide)
            print("Test Precondition Done")
        except WrongDivisionException as e:
            print("We cannot divide by zero", e)
        finally:
            print("Finally Block Executed - Always")


TestException.test_exception_17(0)
