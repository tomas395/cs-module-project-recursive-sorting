# TO-DO: Implement a recursive implementation of binary search

# before a binary search can be implemented, it must be applied to a sorted set of data first

def binary_search(arr, target, start, end):
    # our base case to exit recursion
    if start > end:
        return -1
# setting up the mid point and if the target is lucky enough to be mid, return it
    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
# if the target is beneath the mid point, thats where the start will be and where the search will begin, ignoring the right side
    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
# if not found in the start or mid, the target should be in the end
    else:
        return binary_search(arr, target, mid + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
