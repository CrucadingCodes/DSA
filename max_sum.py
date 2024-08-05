# Maximum sum of i*arr[i]
#  among all rotations of a given array

import sys 

# return max value of i* arr[i]
def maxSum(arr, n):
    # Initialize result
    res = -sys.maxsize

    # Consider rotation beginning with i
    # for all possible values of i.
    for i in range(0,n):
        
        # Initialize sum of current rotation
        curr_sum = 0

        # compute sum of all values
        for j in range(0,n):

            index = (i + j) % n
            # print(arr[index], j , i)
            
            curr_sum += j * arr[index]

        res = max(res, curr_sum)
    return res


arr = [8, 3, 1, 2]
n = len(arr)
print(maxSum(arr, n))
