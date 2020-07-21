# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # divide and conquer
    elements = len(arrA) + len(arrB)
    # * shorthand way place as many zeros in a list by number of elements
    merged_arr = [0] * elements

    # the point is to check the first value of each sub array with the first value of the sub array next to it and swap/merge
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass
