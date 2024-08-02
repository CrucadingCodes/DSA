def m(arr, size):
    max_so_far = float('-inf')
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far  

a = [-2, -3 , 4 , -1, -2, 1, 5, -3]
print("max contiguous sum is", m(a, len(a)))          