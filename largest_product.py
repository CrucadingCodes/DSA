def mul(arr, n):
    result = arr[0]

    for i in range(n):
        mul = arr[i]

        for j in range(i+1, n):
            result = max(result, mul)
            mul *= arr[j]
            # print(result)
        result = max(result, mul) 
    return result

arr = [6, -3, -10, 0, 2]
n = len(arr)
print(mul(arr, n))


# using Kadane's algorithm

def maxProduct(arr, n):

    # max pos product 
    # ending at the current pos
    max_ending_here = arr[0]

    # initialize overall max product
    max_so_far = arr[0]
    # min negative product ending
    # at the current pos
    min_ending_here = arr[0]

    # Traverse through the array
    # the max product subarray ending at an index
    # will be the max of the elemnt itself
    # the product of element and max product ending previously
    # and the min product ending previously

    for i in range(1, n):
        temp = max(max(arr[i], arr[i] * max_ending_here),
                   arr[i]* min_ending_here)
        min_ending_here = min(min(arr[i], arr[i]* max_ending_here),
                              arr[i]* min_ending_here)
        max_ending_here = temp
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(f"Maximum Sub array product is {maxProduct(arr, n)}")    
       
