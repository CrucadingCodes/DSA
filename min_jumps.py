# Minimum number of jumps to reach end (Jump Game)

# using recursion 
# returns min no of jumps to reach arr[h] from arr[l]


def minJumps(arr, l, h):

    # base case when source and destination are same 

    if (h == l):
        return 0
    
    # when nothing is reachable
    # from the given source

    if(arr[l] == 0):
        return float('inf')
    
    # traverse through all the points
    # raechable from point arr[l]
    # recursively get the minimum jumps required to reach arr[h]
    # from these reachable points


    min = float('inf')
    for i in range(l + 1, h + 1):
        if(i < l + arr[l] + 1):
            jumps = minJumps(arr, i, h)
            if (jumps != float('inf') and 
                jumps + 1 < min ):
                min = jumps + 1
    return min

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
print(minJumps(arr, 0, n - 1))       
