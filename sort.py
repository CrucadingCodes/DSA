def sort(arr):
    b = sorted(arr)
    for i in b:
        print(i, end=" ")
   
        
def sort_1(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    for i in arr:
        print(i, end=" ")     

A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sort(A)
print("\n")
sort_1(A)