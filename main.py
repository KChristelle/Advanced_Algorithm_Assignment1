import time

# sockMerchant function to find pairs
start = time.time()


def sock_merchant(n, ar):
    # initialize variable and array
    sock_dict = {}
    counter = 0
    for val in ar:
        if val in sock_dict:
            counter += 1
            sock_dict.pop(val)
        else:
            sock_dict[val] = 1
    return counter


end = time.time()
n = 18
ar = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5]
print(sock_merchant(n, ar))
print("Run time of the function: ", end-start)
