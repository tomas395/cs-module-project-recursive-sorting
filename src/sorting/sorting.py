# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # divide and conquer
    elements = len(arrA) + len(arrB)
    # * shorthand way place as many zeros in a list by number of elements
    merged_arr = [0] * elements
    # initialize the two pointers that start at each list
    a = 0
    b = 0
    # compare both a and b and:
    # if a is bigger, put it the array and loop through both
    # if b is bigger, do the same thing
    # if a is out of range, push b and iterate. if b is out of range, push a and iterate

    # we're making four conditions we need to handle.
    for i in range(elements):  # we're going to iterate over the length of both arrays a and b
        if a >= len(arrA):
            # this is the greater value, so we're going to add sub[b]
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
            # the point is to check the first value of each sub array with the first value of the sub array next to it and swap/merge
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # base condition: when the lists get down to a length of 1
    if len(arr) > 1:  # keep dividing by half
        # find the middle of the array
        # sort in left and place them left of left
        left = merge_sort(arr[0: len(arr) // 2])  # slice and divide list by 2
        # sort in right and place them right of right
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass
