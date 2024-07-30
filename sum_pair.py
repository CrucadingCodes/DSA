def pair(arr, n, K):
    count = 0
    
    for i in range(0,n):
        for j in range(i+1 ,n):
            if arr[i] + arr[j] == K:
                count += 1
                print(arr[i],arr[j])
    return f"number of pairs are: {count}" 

def get_count(arr, sum):
    count = 0
    freq = {}
    
    for num in arr:
        if (sum - num)in freq:
            count += freq[sum- num]
        if num in freq:
            print(num)
            freq[num] += 1
        else:
            freq[num] = 1
    return count

                
arr = [1, 2, -3, 6, 3, -1]     
n = len(arr)
K = 3
sum = 5
# print(pair(arr, n, K))   
print(get_count(arr, sum))  