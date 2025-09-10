a = int(input("Enter your age: "))
if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("you are enter an inalid age")

elif(a==0):
    print("you are entering 0 which is invalid age")

else:
    print("you are below the age of consent") 

print("end of program")