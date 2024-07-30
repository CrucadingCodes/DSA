def missing(n,arr):
    # using hashing
    
    # create a hash of size n+1
    hash = [0] * (n+1)
    
    # store frequencies of elements
    for num in arr:
        hash[num] += 1
        # print(hash[num])
        
    for i in range(1, n + 1):
        if hash[i] == 0:
            return i    
        
    return -1

def missings(n, arr):
    # using first N numbers sum 
    sum_ = sum(arr)
    
    expected_sum = (n * (n+1)) // 2
    
    return expected_sum - sum_ 



arr = [1,2,4,5,6,7]
n = 7
print(missing(n , arr))    
        
    