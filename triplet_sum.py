# Triplet Sum in Array (3sum)

def find( A, n, sum):
    for i in range(0, n - 2):
        for j in range(i + 1, n -1):
            for k in range(j + 1, n):
                if A[i] + A[j] + A[k] == sum:
                    print(A[i], A[j], A[k])
                    return True

    return False


A = [1, 4, 45, 6, 10, 8]
sum = 22
n = len(A)
print(find(A, n, sum))