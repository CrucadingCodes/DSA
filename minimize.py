# Minimize the maximum difference between the heights


def minimize(arr, n, k):
    # sort the array 
    arr.sort()
    ans = arr[n - 1] - arr[0] # max pos height diff 

    for i in range(1, n):
        if arr[i] < k:
            continue

        t_min = min(arr[0] + k, arr[i] - k)

        t_max = max(arr[ i - 1] + k, arr[n - 1]- k)

        ans = min(ans, t_max - t_min)
    return ans

k = 6
n = 3
arr = [1, 15, 10]
ans = minimize(arr, n, k)
print(ans)    

