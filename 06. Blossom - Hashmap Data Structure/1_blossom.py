 ## Hashmaps project - Separate Chaining
 ## Blossom - a hash map that relates the names of flowers to their meanings

# Import the linked list and node library
from linked_list import Node, LinkedList

## Building Out The Hash Map

class HashMap:
  def __init__(self, size):
    # we need to limit the size of the list to make it behave more like an array
    self.array_size = size
## Adding in the Linked List
    # our array will be a python list of LinkedList objects
    self.array = [LinkedList() for item in range(self.array_size)]

    ## implement the methods

    # the internal methods
  def hash(self, key):
    return sum(key.encode())
  def compress(self, hash_code):
    return hash_code % self.array_size

 ## Adding in Separate Chaining: Assignment
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    # save both k\v as a list [key, value]
    payload = [key, value]
    # check if the key exists in the LinkedList before we add our new payload to it
    list_at_array = self.array[array_index]
    # list_at_array should be the LinkedList object instantiated at that location in self.array
    # iterate throught the nodes in the LinkedList
    for node in list_at_array:
      # starting with the head_node, if value = None it means the list is empty
      # or if the saved key matched the key to be assigned
      if node.get_value() == None or node.get_value()[0] == key:
        # overwrite the value saved in the node with the payload
        node.update_value(payload)
        return
    # if the loop is finished without hitting return than the list is not empty but our key is not saved yet
    # we need to add it to our chained list
    list_at_array.insert_beginning(payload)
    #print(list_at_array.stringify_list())

## Adding in Separate Chaining: Retrieval
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    # iterate though the list to check if the keys match
    for node in list_at_index:
      if node.get_value() == None or node.get_value()[0] != key:
        continue
      elif node.get_value()[0] == key:
        # key is found, we return value
        return "The meaning of {f} is '{m}'.".format(f = key, m = node.get_value()[1])
        break
    return "Flower not found!"

## Adding the Flower Definitions
from blossom_lib import flower_definitions

# create a new instance with the length of our definitions list
blossom = HashMap(len(flower_definitions))
# assigning the values
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

# for flower in flower_definitions:
  # print(flower[0])
  # print(flower[1])

# print(flower_definitions)

## try out the app
# look up a flowers meaning
print("\nLooking up the meaning of 'daisy':")
print(blossom.retrieve('daisy'))

print("\nTrying to retrieve a flower thet is not in the HashMap:")
print(blossom.retrieve('nettle'))

# Adding the missing flower
blossom.assign('nettle', 'life and death, protection')
print("\nTrying to look up the missing flower again after assigning it:")
print(blossom.retrieve('nettle'))
