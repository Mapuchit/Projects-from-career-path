 ## Searchcademy - Search Algorithms project

'''
Our company, Searchcademy, uses empty sparsely sorted data to test its awesome search engine. What exactly does that mean?
Sparsely Sorted Data is data such that there is empty data in between the sorted values.

In this project, we will implement a modified version of iterative binary search to search through a sparsely sorted dataset.
'''

 ## Set Up the Function

# A function that searches through data to find the search_val
def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))
  # create two variables (pointers) to store the first and last positions of the dataset
  first = 0
  last = len(data) - 1
  # we will keep iterating until we find our search value
  while first <= last:

 ## Check if the Middle is Empty
    # Here we will continue to loop until we find a value that is not empty
    # We will set the variable mid to equal that value so that we can compare it to search_val in the next step

    # a variable to store the middle index
    mid = (first + last) // 2
    # check if the middle is empty
    if not data[mid]:
      # we will search surrounding values
      # a variable equal to the position directly left of the mid
      left = mid - 1
      # variable equal to the position directly right of the mid
      right = mid + 1
      # a loop that checks if the surrounding values are empty and breaks once we find a non-empty value
      while True:
        # first, we check if we have iterated through the entire dataset and have not found a non-empty value
        # if both left and right are outside the pointer values for the start and end of the list it means we have looked through the entire list
        if left < first and right > last:
          print("{0} is not in the dataset".format(search_val))
          # we can exit the function now
          return
        # now, we will check if the value to the right is not empty
        elif right <= last and data[right]:
          # we set the new middle to be right
          mid = right
          # we can break the inner while loop because we found a non-empty value
          break
        # now, we will check if the value to the left is not empty
        elif left >= first and data[left]:
          # do the same as before
          mid = left
          break
        # if none of the above statements are true it means that the surrounding values are empty, but we haven't checked the entire list yet
        # so we will move our pointers to continue the search
        right += 1
        left -= 1

 ## Check if the Search Value is Equal to the Middle
    # Now that we handled the empty data, let’s continue with regular binary search.
    # We will first check if the middle of the data is equal to our search value.

    if data[mid] == search_val:
      # we print the location where the search_val was found
      print("{0} found at position {1}".format(search_val, mid))
      # and exit the function
      return

 ## Check if the Search Value is Less Than the Middle

    if search_val < data[mid]:
      # we set the end pointer to be 1 less than mid in order to search only the left half of the dataset
      last = mid - 1

 ## Check if the Search Value is Greater Than the Middle

    if search_val > data[mid]:
      # we set the start pointer to be 1 more than mid in order to search only the right half of the dataset
      first = mid + 1

 ## Return "Value not in data"

  # if the outer while loop is finished we have searched the entire dataset without finding search_val
  print("{0} is not in the dataset".format(search_val))



 ## Testing

sparse_search([""], "Hello")
# Hello is not in the dataset
sparse_search(["A", "", "", "", "B", "", "", "", "C"], "B")
# B found at position 4
sparse_search(["A", "", "", "", ""], "A")
# A found at position 0
sparse_search(["", "", "", "", "Z"], "Z")
# Z found at position 4
sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "C")
# C found at position 8
sparse_search(["A", "B", "", "", "E"], "A")
# A found at position 0
sparse_search(["", "X", "", "Y", "Z"], "Z")
# Z found at position 4
sparse_search(["A", "", "", "", "B", "", "", "", "C"], "D")
# D is not in the dataset
sparse_search(["Apple", "", "Banana", "", "", "", "", "Cow"], "Banana")
# Banana found at position 2
sparse_search(["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"], "Parth")
# Parth found at position 18
