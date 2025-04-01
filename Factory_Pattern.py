class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    pets = dict(dog=Dog(), cat=Cat())
    return pets[pet]

d = get_pet("dog")
print(d.speak())  # Output: Woof!

c = get_pet("cat")
print(c.speak())  # Output: Meow!
