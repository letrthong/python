text = 'Geeks'
iterable_obj = iter(text) 
  
while True: 
    try: 
        item = next(iterable_obj) 
        print(item) 
    except StopIteration: 
        break

print("") 
size= len(text)   
for i in range(size): 
    print( text[i]) 