def quicksort(arr):
    """
    parameters:
    ---------------
    arr: arr
    the arrnge you need to sort
    """
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,1,3,4,5,3,6,4,8,9,7]))

