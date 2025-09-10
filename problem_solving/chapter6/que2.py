# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
name=str(input("enter student name: "))
sub1 = int(input("enter obtsined in phy by " + name +":"))
if(sub1>33):
    print("pass in phy")
else:
    print("fail in phy")
sub2 = int(input("enter obtsined in che by " + name + ":"))
if(sub2>33):
    print("pass in che")
else:
    print("fail in che")
sub3 = int(input("enter obtsined in math by " + name +":"))
if(sub3>33):
    print("pass in math")
else:
    print("fail in math")
tmarks=(sub1+sub2+sub3)/3
if(tmarks>40):
    print(name +" is passed")
else:
    print("fail in total sub")