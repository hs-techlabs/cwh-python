# Write a program to calculate the factorial of a given number using for loop.
n = int(input("Enter a number: "))
i = 1
fac = 1
while(i<=n):
    fac*=i
    i+=1
print(fac)