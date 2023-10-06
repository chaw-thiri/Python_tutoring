num1= int(input("Type a number"))
num2= int(input("Type a number"))
num3 = int(input("Type a number"))
num4 = int(input("Type a number"))
num5 = int(input("Type a number"))
num_list = []
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)
num_list.append(num5)

smallest = 1000000  # give the largest number possible, so that it could be replaced in for loop
for i in range(len(num_list)):
    if num_list[i] < smallest:
        smallest = num_list[i]
print(smallest)