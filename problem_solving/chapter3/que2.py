# name=str(input("Enter your name:"))
# date=int(input("Enter your date of selection:")) 
# print=(f"Dear {name} You are selected {date}" )
       
letter='''Dear <|name|>,
         You are selected! 
         <|date|> '''

print(letter.replace("<|name|>","himanshu").replace("<|date|>","14 nov 2003"))