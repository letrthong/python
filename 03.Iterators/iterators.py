text = 'Geeks'
iterable_obj = iter(text) 
  
while True: 
    try: 
  
        # Iterate by calling next 
        item = next(iterable_obj) 
        print(item) 
    except StopIteration: 
        # exception will happen when iteration will over 
        break

print("") 
size= len(text)   
for i in range(size)  : 
    print( text[i]) 