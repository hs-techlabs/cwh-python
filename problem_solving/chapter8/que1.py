# Write a program using functions to find greatest of three numbers. 
a=1
b=8
c=6

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a=1
b=8
c=6
print(greatest(a,b,c))