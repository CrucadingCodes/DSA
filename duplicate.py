def duplicates(nums):
    n = max(nums) # get the max num of the input list 
    
    # create an aux list of size n+1 initialized to 0
    arr = [0] * (n + 1)
    # print(arr)
    result = [] # list to store duplicates
    
    # iterate through each number in the input list
    
    for num in nums:
        # print(num)
        arr[num] += 1 # increment the count for this number
        # print(arr[num])
        if arr[num] == 2: # check if it's a duplicate 
            result.append(num) # if a duplicate add to list
    
    return result

nums = [1, 12, 2, 4 ,1, 8, 2, 7, 9 ] 
res = duplicates(nums)
print("duplcates are", end=" ")
for i in res:
    print(i, end=" ")
print()        
    
    
    
    