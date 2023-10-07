# I am clear of the question
# supposing to print the number in reverse direction
# input = 10
# output = 10 9 8 7 6 5 4 3 2 1

num = int(input("Number : "))

for i in range(num, 0, -1):  # start, end, direction
    # default direction : 1  (ascending)
    #                     -1 (descending)
    print(i)