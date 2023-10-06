num_list =input("Number :").split()  
# input = "1 2 3 4 5"
# split() break the input string at " " and put them into a list.   >> ["1", "2" , "3" , "4" , "5"]

for i in range(len(num_list)):  # ["1", "2" , "3" , "4" , "5"] >> [1,2,3,4,5]
    num_list[i] = int(num_list[i])
#print(num_list)    << check the final list here.

smallest = 1000000  # give the largest number possible, so that it could be replaced in for loop
for i in range(len(num_list)):
    if num_list[i] < smallest:
        smallest = num_list[i]
print(smallest)