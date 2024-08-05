def longest(arr, n):

    ans = 0
    count = 0

    # sort the array
    arr.sort()

    v = []
    v.append(arr[0])

    # insert repeated elements only 
    # once in the vector
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])

    # find max length
    # by travesing the array
    for i in range(len(v)):

        # check if the current elemnet is 
        # equal to the previous element +1
        if (i >0 and v[i]== v[i-1]+ 1):
            count += 1
            
        else:
            count = 1

        ans = max(ans,count) 
    return ans                   