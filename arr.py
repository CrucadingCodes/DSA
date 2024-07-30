# decleration of an array 

import array

'''arr = array.array('i') # will store only integer type element
arr = array.array('b') # will store only char type element
arr = array.array('f') # will store only float type element

print (arr)


# initialization of an array

arr = array.array('i', [1,2,3,4,5]) # store only integer type element
print (arr)



# traversal in array 
for i in arr:
    print (i)
    print (i, end=" ")'''
    
# insertion in array
# prog to insert an element at a specific position in an array


# case 1 : static array 
def insert(arr, n, x, pos):
    
    # shift elements to the right
    # which are on the right side of the position
    
    for i in range(n-1, pos-1, -1):
        arr[i + 1] = arr[i] # right shift

    arr[pos] = x

# case 2: dynamic arr 
def insert_1(arr, x, pos):
    n = len(arr)
    arr.append(0)
    
    for i in range(n-1, pos-1, -1):
        arr[i + 1] = arr[i]
        
    arr[pos] = x

arr = [10, 12, 14, 16, 18]   
arr_ = [10, 12, 14, 16, 18]           
n = 4 # 4 # current elements in arr
x = 15
pos = 3


print("Before insertion", arr)
insert(arr, n, x, pos)
print("After insertion", arr)
insert_1(arr_, x, pos)
print("After insertion", arr_)

# deleting an array element

# function to find for a key in the arr

def search(arr, key, n):
    for i in range(0, n):
        if arr[i] == key:
            return i
    return -1

def delete(arr, key, n):
    pos = search(arr, key, n)

    if pos == -1:
        print("Element not found")
    else:
        for i in range(pos, n-1):
            arr[i] = arr[i + 1] # left shift
    return n - 1  # return new length of arr


arr = [10, 12, 14, 16, 18]
n = len(arr)
key = 14
print("Before deletion", arr)
new_length = delete(arr, key, n)
arr = arr[:new_length]
print("After deletion", arr)

   
    


