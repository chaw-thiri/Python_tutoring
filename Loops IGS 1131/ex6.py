num = int(input("Type a positive number : "))
while (num <= 0): # as a
    num = int(input("Number for factorial shouldn't be a negative or zero.\nEnter a new number: "))
result = 1
# start = 1 (1 for multiplication problems)
for i in range(1,num+1): # ascending >> (start, end + 1)
    result *= i
print(result)
