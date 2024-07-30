def occurance(arr, n, k):
    count = 0
    for i in range(n):
        if arr[i] == k:
            count += 1
    return count

arr = [10, 20, 20, 10, 10, 20, 5, 20]
n = len(arr)
k = 20
print(occurance(arr, n, k))