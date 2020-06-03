import random

# The code for performing bubble sort on an array of numbers is provided below.
# However, we are sorting on books which are Python dictionaries. Further, the owner likes to change the ordering of books daily.

# To make the sort order flexible, we add an argument comparison_function.
# This will allow us to pass in a custom function for comparing the order of two books.
# Our comparison_function will take two arguments, and return True if the first one is “greater than” the second.

def bubble_sort(arr, comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      # we modify the comparison conditional statement to use the comparison_function
      # instead of the built in operators (if arr[idx] > arr[idx + 1]:)
      # the comparison_function's arguments will index into the individual book dictionaries in the bookshelf list of dictionaries
      if comparison_function(arr[idx], arr[idx + 1]):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr

# The code for quicksort of a numeric array is provided below.
# We need to modify it in a similar fashion that we modified bubble sort, to be able to use on a list of dictionaries.

# We add the comparison_function as the final argument.
def quicksort(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    # we update the comparison conditional to use the comparison_function
    # instead of the built in comparison (if pivot_element > list[i]:)
    if comparison_function(pivot_element, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  # we pass the comparison_function as argument to the recursive calls too
  quicksort(list, start, less_than_pointer - 1, comparison_function)
  quicksort(list, less_than_pointer + 1, end, comparison_function)
