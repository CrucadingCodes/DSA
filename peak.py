def peak(arr,n):
    
    # first or last element is peak 
    if (n ==1):
        return 0
    if(arr[0]>=arr[1]):
        return 0
    if(arr[n-1]>=arr[n-2]):
        return n-1
    
    # check for every other element 
    for i in range(1,n-1):
        if (arr[i]>=arr[i-1] and arr[i]>=arr[i+1]):
            return "the peak element is",arr[i], "at index",i
    return -1

arr = [10, 20, 15, 2, 23, 90, 67]
n = len(arr)

print(peak(arr,n))