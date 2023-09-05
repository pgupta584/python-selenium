# Classes are nothing but blueprint/prototype where all the related functions will be kept
# Take one example
class Engine:  # Create class using class <ClassName>
    def start_engine(self):  # Nonstatic method, will understand self in upcoming session
        print("Engine Started")

    @staticmethod
    def stop_engine():  # Static method
        print("Engine Stopped")


# Create object --> we just give class not in other language we use new keyword like new <ClassName>();
obj = Engine()
obj.start_engine()
obj.stop_engine()
# We can directly also call
print("********")
Engine().start_engine()
Engine().stop_engine()
