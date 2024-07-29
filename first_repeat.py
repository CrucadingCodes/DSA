def repeat(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return arr[i]

    return -1

arr = [1, 2, 3, 2, 4, 2, 5]
n = len(arr)

index = repeat(arr, n)

if index == -1:
    print("No repeating element")
else:
    print("The repeating element is", arr[index])    