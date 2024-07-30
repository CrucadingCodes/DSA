def subarray_sum(arr, n, target_sum):
    res = [] # to store the  result
    
    # flag to indicate if subarray is found 
    flag = False
    
    for i in range(n):
        current_sum = arr[i] # initialize current_sum
        
        # check if single element is the sum 
        if current_sum == target_sum:
            res.append(i+1)
            # res.append(i+1)
            flag = True
            break
        else:
            # try all subarrays starting with 'i'
            for j in range(i+1, n):
                current_sum += arr[j]
                if current_sum == target_sum:
                    res.append(i+1)
                    res.append(j+1)
                    flag = True
                    break
            if flag:
                break
    if flag:
        return res
    return [-1]     # if not subarray is found   


# using a sliding window (to reduce time complexity)
def sum(arr, n, tar_sum):
    last = 0
    start = 0
    cursum = 0
    flag = False
    res = []
    
    for i in range(n):
        # store sum up to current element
        cursum += arr[i]
        
        # check if current sum is greater than or equal to given number
        
        if cursum >= tar_sum:
            last = i
            
            # start from starting index till current index
            while target_sum < cursum and start < last:
                
                # subtract the element from left
                cursum -= arr[start]
                start += 1
            # if cur sum equals to given num    
            if cursum == tar_sum:    
                res.append(start + 1)
                res.append(last + 1)
                flag = True
                break
    if not flag:
        res.append(-1)
    
    return res            
        


if __name__ == "__main__":
    arr = [1,2,3,7,5]
    n = len(arr)
    target_sum = 17
    # result = subarray_sum(arr, n, target_sum)
    re = sum(arr, n, target_sum)
    for i in re:
        print(i, end=" ")