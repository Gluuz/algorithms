# 4.1 Sum function
def sum(arr):
    # Base case: If the array is empty, return 0
    if len(arr) == 0:
        return 0
    # Base case: If the array has only one element, return that element
    elif len(arr) == 1:
        return arr[0]
    else:
        # Recursive case: Return the sum of the first element and the sum of the rest of the array
        return arr[0] + sum(arr[1:])


# 4.2 Count number of items in a list
def count(arr):
    # Base case: If the array is empty, return 0
    if len(arr) == 0:
        return 0
    else:
        # Recursive case: Return 1 plus the count of the rest of the array
        return 1 + count(arr[1:])  # [1:] means from the second item to the end


# 4.3 Maximum number in a list
def max(arr):
    # Base case: If the array has only one element, return that element
    if len(arr) == 1:
        return arr[0]
    # Base case: If the array is empty, return an error message
    elif len(arr) == 0:
        return "error: list must contain at least one number!"
    else:
        # Recursive case: Find the maximum number between the first element and the maximum of the rest of the array
        sub_max = max(arr[1:])
        return sub_max if sub_max > arr[0] else arr[0]


# Quicksort code
def quicksort(arr):
    # Base case: If the array has less than two elements, it's already sorted
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        # Create a sub-array consisting of elements less than or equal to the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # Create a sub-array consisting of elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]
        # Recursively sort the sub-arrays and concatenate them with the pivot in between
        return quicksort(less) + [pivot] + quicksort(greater)
