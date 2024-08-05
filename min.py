def findmin(arr, n):
    min_ele = arr[0]

    #traversing over array to 
    # find minimum element
    for i in range(n):
        if arr[i] < min_ele:
            min_ele = arr[i]

    return min_ele   
arr = [3, 4, 8, 2, 6]
n = len(arr)
print(findmin(arr, n))     