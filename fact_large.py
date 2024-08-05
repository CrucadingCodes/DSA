import sys

# this func finds factorial of large nums and prints them
'''def fact(n):
    res = [None] * 500

    res[0] = 1
    res_size = 1

    # apply simple fact formula 
    x = 2
    while x<=n:
        res_size = multiply(x, res, res_size)
        x += 1

    print("factorial of a given number is")
    i = res_size - 1
    while i >= 0:
        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
        i -= 1


# this func multiplies x with num
# represented by res[]. res_size is size of res[]
# or number of digits in the number represented
# by res[]. This function uses simple school
# mathematics for multiplication. This function
# may value of res_size and returns the new value
# of res_size


def multiply(x, res, res_size):

    carry = 0 # initialize carry
    # one be one multiply n with individual digits of res[]

    i = 0 
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod # store last digit of prod in res[]
        # make sure floor division is used 
        # to avoid floating value 
        carry = prod // 10
        i += 1

    # Put carry in res and increase result size
    while (carry):
        res[res_size] = carry % 10
        # make sure floor division is used
        # to avoid floating value
        carry = carry // 10
        res_size += 1
    return res_size'''
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
        # print(f)
    return f
print(factorial(100))




