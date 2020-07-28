#
# FileName: recursion.py
#
    
def countWithFor(n):
    sum = 0
    for x in range(n): #  Range: 0 to n-1
        sum = sum + (x+1)
    return sum


def countWithRecursion(n):
    if n < 1: 
        return 0
    else :
        return n + countWithRecursion(n-1)


number = 5; # 1+2+3+4+5
i = countWithFor(number);  
print i
i = countWithRecursion(number); 
print i


