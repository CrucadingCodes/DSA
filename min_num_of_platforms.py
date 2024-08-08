# Minimum Number of Platforms 
# Required for a Railway/Bus Station

def findPlatforms(arr, dep, n):
    # plat_needed indicates no of platforms
    # needed at a time
    plat_needed = 1
    result = 1

    # run a nested loop to find overlap
    for i in range(n):
        plat_needed = 1

        for j in range(n):
            if i != j:
                if (arr[i] >= arr[j]and dep[j] >= arr[i]):
                    plat_needed += 1
        result = max(result, plat_needed) 
    return result
def Platfroms(arr, dep, n):
    arr.sort()
    dep.sort()

    plat_needed = 1
    result = 1
    i = 1
    j = 0

    while (i < n and j < n):
        if (arr[i] <= dep[j]):
            plat_needed += 1
            i += 1

        elif (arr[i] > dep[j]):
            plat_needed -= 1
            j += 1

        if (plat_needed > result):
            result = plat_needed
    return result                

def main ():
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    n = len(arr)
    print("Minimum Number of Platforms Required = ",findPlatforms(arr, dep, n))

if __name__ == "__main__":
    main()    
               
