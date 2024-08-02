# using nested loops
def sub(arr, n):
    for i in range(n):
        # starting point of the subarray and
        # sum in initialized with the first element of subarray 

        sum = arr[i]

        if sum == 0:
            return True
        
        for j in range(i+1, n):
            # we are finding the sum till the jth index
            # starting for the ith index
            sum += arr[j]
            if sum == 0:
                return True
    return False

# using hashing

def sub_(arr,n):
    # traverse through array
    # and store prefix sums
    n_sum = 0
    s = set()

    for i in range(n):
        n_sum += arr[i]

        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
    return False

arr = [4, 2, -3, 1, 6] 
n = len(arr)

if sub_(arr, n):
    print("found a subarray with 0 sum")
else:
    print("No subarray with 0 sum")    
