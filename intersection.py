def intersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j< n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        
        else: 
            print(arr2[j], end=" ")
            i += 1
            j += 1
            
arr1 = [1,2,3,2,4,5]
arr2 = [2,3,5,7]

m = len(arr1)
n = len(arr2)

intersection(arr1, arr2, m, n)
                    