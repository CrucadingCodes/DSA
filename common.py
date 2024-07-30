def common(A, B, C):
    i, j, k = 0, 0, 0
    
    common = []
    
    # iterate through three arrays while all arrays have elements
    
    while i < len(A) and j < len(B) and k < len(C):
        
        if A[i] == B[j] and B[j] == C[k]:
            common.append(A[i])
            
            i += 1
            j += 1
            k += 1
            
            # skip duplicate elements in A
            while i < len(A) and A[i] == A[i-1]:
                i += 1
            
            # skip duplicate elements in B
            while j < len(B) and B[j] == B[j-1]:
                j += 1
            
            # skip duplicate elements in C
            while k < len(C) and C[k] == C[k-1]:
                k += 1
        
        # if A[i] < B[j], then ith element can't be common
        elif A[i] < B[j]:
            i += 1                
        
        # if B[j] < C[k], then ith element can't be common
        elif B[j] < C[k]:
            j += 1
        
        # if C[k] is smallest then kth element can't be common
        else:
            k += 1
            
    return common



# Sample Input
A = [1, 5, 10, 20, 30]
B = [5, 13, 15, 20]
C = [5, 20]

comm = common(A, B, C)
print("common elements:", end =" ")

for e in comm:
    print(e, end =" ")
         
        
            