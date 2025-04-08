class BaseClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from BaseClass, {self.name}!")

class NewClass(BaseClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print(f"Hello from NewClass, {self.name}. You are {self.age} years old.")

# Create an instance of the new class
new_instance = NewClass("World", 25)

# Run the method
new_instance.greet()
