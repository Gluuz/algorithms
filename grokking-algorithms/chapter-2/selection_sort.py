# Finds the smallest value in an array
def findSmallest(array):
  # Stores the smallest value
  smallest = array[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(array)):
    if array[i] < smallest:
      smallest_index = i
      smallest = array[i]      
  return smallest_index

# Sort array
def selectionSort(arr):
  new_array = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      new_array.append(arr.pop(smallest))
  return new_array