 ## A Sorted Tale - Sorting Algorithms project
 ## Sorting books in a bookshop


'''
You recently began employment at “A Sorted Tale”, an independent bookshop. Every morning, the owner decides to sort the books in a new way.
Some of his favorite methods include:

    By author name
    By title
    By number of characters in the title
    By the reverse of the author’s name

Throughout the day, patrons of the bookshop remove books from the shelf.
Given the strange ordering of the store, they do not always get the books placed back in exactly the correct location.
The owner wants you to research methods of fixing the book ordering throughout the day and sorting the books in the morning.
It is currently taking too long!
'''

## Get to know the data

# The owner provides the current state of the bookshelf in a comma-separated values, or csv, file.
# We have a larger file that contains all the books in the bookshop and a smaller file with 10 books that we'll use to test the algorithm.
# A function to read the data from the csv's is defined in utils.py

import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# Print all the books in the small bookshelf loaded above to check that our load_books function works.
print("\nThe small bookshelf has the below books:")
for book in bookshelf:
  print(book["title"])

# After printing we see that today's sorting it by title, but some patrons have placed books back in slightly the wrong place, so we need to re-organise them
print("\nThe books seem to be organised by titles but some are at the wrong place.")

print("\nIn order to compare the titles we need to know how to compare characters code points in Python:")
# Python’s built-in comparison operators compare letters lexicographically based on their Unicode code point.
# You can determine the code point of characters using Python’s built-in ord function.
print("The code point of the letter 'a' is: {}".format(ord("a")))
print("The code point of the character ' ' is: {}".format(ord(" ")))
print("The code point of the letter 'A' is: {}".format(ord("A")))

# When sorting, we don’t want to take into account the case of the letters. For example, “cats” should come before “Dogs”, even though ord("c") > ord("D") is True.
# We’ll make this happen by converting everything to lowercase prior to comparison.
# We modify the loader function in utils.py to add the lower case author and title to each books dictionary
print("\nThe lower case titles are:")
for book in bookshelf:
  print(book["title_lower"])

## Fix the midday errors

# As we noted, our books are pretty close to being sorted by title.
# Bubble sort performs well for nearly sorted data such as this.
print("\nUsing Bubble Sort on the nearly sorted small bookshelf:")
# The code for performing bubble sort on an array of numbers is provided in sorts.py.
# We modified the bubble_sort function to take in as argument a comparison_function that compares two books

# We define here the comparison_function that takes two book dictionaries as arguments
def by_title_ascending(book_a, book_b):
  # it returns True if the title_lower of book_a is “greater than” the title_lower of book_b
  # meaning that book_a's title should come AFTER book_b's title in an alphabetical order and we need to swap the books
  return book_a["title_lower"] > book_b["title_lower"]

# Now we can sort the smaller bookshelf using bubble sort and the helper comparison_function

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
# There were 2 swaps
print("\nThe small bookshelf has been reorganised:")
for book in sort_1:
  print(book['title'])

## A new sorting order

# The owner of the bookshop wants to sort by the author’s full name tomorrow.
# We create a new helper comparison_function for this purpose
def by_author_ascending(book_a, book_b):
  # it returns True if the author_lower of book_a is “greater than” the author_lower of book_b
  # meaning that book_a's author should come AFTER book_b's author in an alphabetical order and we need to swap the books
  return book_a["author_lower"] > book_b["author_lower"]

# Our sorting algorithms will alter the original bookshelf, so we create a new copy of this data.
bookshelf_v1 = bookshelf.copy()

# Try sorting the list of books, bookshelf_v1 using the new comparison function and bubble sort.
print("\nUsing Bubble Sort on the original small bookshelf to sort by author:")
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
# There were 26 swaps
print("\nThe small bookshelf has been reorganised by author name:")
for book in sort_2:
  print(book['author'])

## A new sorting algorithm

# The number of swaps is getting to be high for even a small list like this.
# Let’s try implementing a different type of search: quicksort.
# The code for quicksort of a numeric array is in sorts.py.
# We need to modify it in a similar fashion that we modified bubble sort.

# We updated the quicksort function with a comparison_function argumant.
# So that it is now able to handle the list of dictionaries that is bookshelf

# To try quicksort we create another copy of bookshelf
bookshelf_v2 = bookshelf.copy()

# Perform quicksort on bookshelf_v2 using by_author_ascending.
# This implementation operates on the input directly, so does not return a list.
print("\nUsing Quicksort on the original small bookshelf to sort by author:")
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
# There were 17 swaps with quicksort
print("\nThe small bookshelf has been reorganised by author name:")
for book in bookshelf_v2:
  print(book['author'])

## The last sort

# The owner has asked for one last sorting order:
# Sorting by the length of the sum of the number of characters in the book and author’s name.

# We create a new comparison_function:
# It should return True if the sum of characters in the title and author of book_a is “greater than” the sum in book_b
def by_total_length(book_a, book_b):
  return len(book_a["title_lower"]) + len(book_a["author_lower"]) > len(book_b["title_lower"]) + len(book_b["author_lower"])

# Load the long list of books into a new variable, long_bookshelf.
long_bookshelf = utils.load_books("books_large.csv")

# Run bubble sort on this algorithm using by_total_length as the comparison function. Does it seem slow?
print("\nUsing Bubble Sort to order long_bookshelf by total length:")
sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
# Yes it took a few seconds. There were 1092069 swaps

# Now try Quicksort:
print("\nUsing Quicksort to order long_bookshelf by total length:")
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
# It sorts instantaneously compared to the few seconds it took for bubble_sort

# Sorting the long_bookshelf by title.
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_title_ascending)

for book in long_bookshelf:
  print(book["title"] + " by " + book["author"])
