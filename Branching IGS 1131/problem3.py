# year % 4 == 0: 
# This checks if the year is evenly divisible by 4.
# If it is, then it's a potential leap year because leap years are typically divisible by 4.

# year % 100 != 0: 
# This part checks if the year is not evenly divisible by 100.
# If a year is divisible by 100, it's not a leap year, unless...

# (year % 400 == 0): This condition checks if the year is evenly divisible by 400.
# If it is, then it overrides the condition in step 2. In other words, if a year is divisible by 400, it is considered a leap year, even though it's divisible by 100.

# test cases : 300, 2012


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
    
