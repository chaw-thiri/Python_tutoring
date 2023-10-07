

# a number is a prime number if it is not divible by any number except 1 and itself. so end = num -1 
# every number is divisible by 1
# so start = 2 , end = num -1 
# 
# special case : 1, 2,3 
# 1 is not a prime no, 2 is a prime number 
num = int(input("Enter a number "))
# prime numbers  = 2,3,5,7,11,13
if num <= 1:
    print(num, "Not prime")
else:
    is_prime = True  # assume num is prime

    # Check for divisors from 2 to num - 1
    for i in range(2, num): #  range(start, end+ 1) , end = num - 1 , so 1 cancel out each other
        if num % i == 0:
            is_prime = False  # num is divisible by i, so it's not prime
            break  # No need to continue checking
        
    if is_prime == True: 
        print("Prime")
    else:
        print("Not Prime")

# ** think with 2 as a test case 
    

