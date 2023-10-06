# if you want to use single line input
num_list =input("Number :").split()  
# input = "1 2 3 4 5"
# split() break the input string at " " and put them into a list.   >> ["1", "2" , "3" , "4" , "5"]

for i in range(len(num_list)):  # ["1", "2" , "3" , "4" , "5"] >> [1,2,3,4,5]
    num_list[i] = int(num_list[i])
#print(num_list)    << check the final list here.

lowest_num = min(num_list) # get the smallest number 
print(lowest_num)
