# function to find the partition position
def partition(arr, low, high):
    # choose the rightmost element as pivot 
    pivot = arr[high] 
    
    # pointer for greater element
    i = low -1
    
    # traverse through all elements 
    # compare each element with pivot
    
    for j in range(low, high):
        if arr[j] <= pivot:
            
            # if element smaler than pivot is found 
            # swap it with the greater elemented pointed by i
            
            i = i + 1
            
            # swapping elementt at i with element at j 
            (arr[i], arr[j]) = (arr[j], arr[i])
            
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # return the position from where partition is done        
    return i+1         

# function to perform quick sort
def quicksort(arr, low, high):
    if low < high:
        
        # find pivot element such that 
        # elemnt smaller than pivot are on the left 
        # elemnt greate than pivot are on the right
        
        pi = partition(arr, low, high)
        
        # recursively call on the left of the pivot
        quicksort(arr, low, pi - 1)
        
        # recursively call on the right of the pivot 
        quicksort(arr, pi + 1, high)
        
        
array = [ 10, 7, 8, 9, 1, 5]
N = len(array)

quicksort(array, 0, N - 1)
print('sorted array :')
for x in array:
    print(x, end =" ")
        
    