# sum of the lengths of any two sides must >= length of the third side. 
a = float(input("side a: "))
b = float(input("side b: "))
c = float(input("side c: "))

# Check if it's a valid triangle
if ((a + b > c)and (a + c > b) and (b + c > a)):
    print("Valid")
else:
    print("Invalid")
