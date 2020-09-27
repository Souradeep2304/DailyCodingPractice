
# Python3 code to demonstrate  
# smallest number greater than K 
# using naive method  
  
# Initializing list  
test_list = [1, 4, 7, 5, 10] 
  
# Initializing k 
k = 6
  
# Printing original list  
print ("The original list is : " + str(test_list)) 
  
# Using naive method  
# to find smallest number 
# greater than K 
min_val = 0
for i in test_list : 
    if min_val < i and i < k : 
        min_val = i 
  
# Printing result  
print ("The minimum value greater than 6 is : " + str(min_val)) 