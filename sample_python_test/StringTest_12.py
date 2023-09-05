# Inheritance --> Acquire the property of parent class in child
# Take one example
from sample_python_test.ConstructorTest_10 import Calculator


# Explain Import how does it work

class ChildClass(Calculator):  # To inherit pass the Class name in small brackets
    class_variable_2 = 20

    def __init__(self):  # We need to create a default constructor & call parent constructor here
        Calculator.__init__(self, 5, 10)

    def add_all(self):
        print("Addition of all is --> ")
        return self.class_variable_2 + self.class_variable + self.add_numbers()
    # Since here we are calling Instance variable we need to call constructor of parent to assign a & b
    # Else a & b from where it will come, since a & b is dynamically passing at the time of object creation


# Create object --> we just give class not in other language we use new keyword like new <ClassName>();
child_obj = ChildClass()
print(child_obj.add_all())
