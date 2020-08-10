text = 'Geeks'
iterable_obj = iter(text) 
  
while True: 
    try: 
        item = next(iterable_obj) 
        print(item) 
    except StopIteration: 
        break

print("")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

while True: 
    try: 
        item = next(myit) 
        print(item) 
    except StopIteration: 
        break

print("") 
cars = ["Ford", "Volvo"]
sizeOfCar=len(cars)

carIt = iter(cars)
for i in range(sizeOfCar): 
    item = next(carIt) 
    print(item) 


print("") 
size= len(text)   
for i in range(size): 
    print( text[i]) 