# solved using len of the string 
# would not work for decimal inputs

num = input("Number : ")
if (len(num) >= 3 ): # len () check the length of the string
    # len() can only apply on strings and lists
    print("Yes")
else: print("No")