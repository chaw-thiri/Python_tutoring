# *     start = 1
# **
# ***
# ****
# ***** end = 5
# ---------------------------------------------division line 
# **** start = 4
# ***
# **
# *   end = 1
# When you see a triangle, break it into two parts; normal triangle and inverted triangle 
# and use a loop for each triangle
for i in range(1,6): # range(start, end+1)  ,
    print("*"*i)
for i in range(4, 0, -1): # range(start, end -1, descending)
    print("*"*i)
