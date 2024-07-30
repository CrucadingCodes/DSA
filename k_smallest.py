def kSmallest(arr, N, K):
    arr.sort()
    
    return arr[K-1]

arr = [12, 3, 5, 7, 19]
N = len(arr)
K = 2
print(kSmallest(arr, N, K))