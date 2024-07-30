def array(arr1, arr2, m, n):
    set1 = set(arr1)
    set2 = set(arr2)
    
    result = list(set1.union(set2))
    
    return result

def union(arr1, arr2, m, n):
    i,j = 0, 0
    
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i], end = " ")
            i += 1
        
        elif arr2[j] < arr1[i]:
            print(arr2[j], end = " ") 
            j += 1
        
        else:
            print(arr2[j], end = " ")
            j += 1
            i += 1
            
    while i < m:
        print(arr1[i], end = " ")
        i += 1
    while j < n:
        print(arr2[j], end = " ")
        j += 1

arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
union(arr1, arr2, m, n)                  