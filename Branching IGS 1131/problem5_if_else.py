num1= int(input())
num2= int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

# it is important to click "enter " after every number or you will get an error
if ((num1 < num2) & (num1 < num3) & (num1 < num4) & (num1< num5)):
    smallest = num1
elif ((num2 < num3) & (num2 < num4) & (num2 < num5)):
    smallest = num2
elif ((num3 < num4) & (num3 < num5)):
    smallest = num3
elif ((num4 < num5)):
    smallest = num4
else: 
    smallest = num5
    
    
    
print("Smallest",smallest)