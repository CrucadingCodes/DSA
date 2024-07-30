def rotate(arr, n):
    last_el = arr[n - 1]
    # print(last_el)
    for i in range(n-1, 0, -1):
        arr[i] = arr[i - 1]
        
    arr[0] = last_el
    # print(arr[0])
    return arr
    



def rotated(arr, n):
    i = 0
    j = n-1
    # 
    while i != j:
        arr[i], arr[j] = arr[j], arr [i]
        i += 1
    pass 
    return arr    
    
arr = [2,6,3,10,7]
n = len(arr)
print(rotated(arr, n))          
        