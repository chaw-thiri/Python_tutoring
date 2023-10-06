num = float(input("Enter your number: "))
result = 0 
if (num > 100):
    if ((num %3 == 0 ) and(num % 2 == 0 )): # num is divisible by both 3 and 2
        result += 18
        
     # this elif will enter only if the num is divisible by 3 but not 2
    elif (num % 3 == 0): # divisible by 3 
        result += 3
        result *= 2   # due to the last statement
        """ if it is divisible by one of 2 or 3, but not the other one. then multiply the result with the number it is not divisible by"""
        
    # this will enter only if the num is divisible by 2 but not 3    
    elif (num % 2 == 0): # divisible by 2
        result += 2
        result *= 3
        
    else :  # num divisible by none.
        result -= 11
        
else:
    if ((num %3 == 0 ) and(num % 2 == 0 )): # num is divisible by both 3 and 2
        result -= 18
        
     # this elif will enter only if the num is divisible by 3 but not 2
    elif (num % 3 == 0): # divisible by 3 
        result -= 3
        result /= 2   # due to the last statement
        """ if it is divisible by one of 2 or 3, but not the other one. then multiply the result with the number it is not divisible by"""
        
    # this will enter only if the num is divisible by 2 but not 3    
    elif (num % 2 == 0): # divisible by 2
        result -= 2
        result /= 3
        
    else :  # num divisible by none.
        result += 11
print("Result :", result)
    