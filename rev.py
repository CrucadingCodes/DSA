def reverse(A,start, end):
    # reversed_arr = A[::-1]
    # for i in reversed_arr:
    #     print(i, end=" ")
    while start<end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    return A

A = [1,2,3,4,5]
print(reverse(A,0,4))