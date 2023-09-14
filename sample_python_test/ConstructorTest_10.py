# Constructors are special function which execute at the time of object creation.
# Constructor will be the first function to get call inside a class like in java once object get created
# Self keyword is mandatory while calling variables into function
# Take one example
class Calculator:  # Create class using class <ClassName>
    class_variable = 10  # This is class variable which will remain same for the class

    # Example 1
    # def __init__(self):
    #     print("I am default Constructor")

    # Here self is nothing but Object ,when We create Object like obj = Calculator(10, 5)
    # this obj will be passed to self & self.a=a will assign the value
    # Here a & b are instance variable which will be changed at run time
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_number(self, a, b):
        print("Addition is --> ")
        return a + b

    def add_numbers(self):
        print("Addition is --> ")
        # return self.a + self.b + self.class_variable # Both way we can do
        return self.a + self.b + Calculator.class_variable


# Create object --> we just give class not in other language we use new keyword like new <ClassName>();
obj = Calculator()
print(obj.add_number(10, 1))
