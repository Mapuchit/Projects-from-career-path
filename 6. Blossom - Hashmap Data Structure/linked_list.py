class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node
  def __repr__(self):
    return str(self.value)

  def set_next_node(self, next_node):
    self.next_node = next_node
  def get_next_node(self):
    return self.next_node

  def get_value(self):
    return self.value
  def update_value(self, new_value):
    self.value = new_value

class LinkedList:
  def __init__(self, value = None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

  ## making the class iterable
  # override __iter__() function inside our class
  def __iter__(self):
    current_node = self.head_node
    while current_node is not None:
      yield current_node
      current_node = current_node.get_next_node()

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    node = self.get_head_node()
    nodes_string = ""
    while node.get_next_node() != None:
      nodes_string += str(node.get_value()) + "\n"
      node = node.get_next_node()
    nodes_string += str(node.get_value()) + "\n"
    return nodes_string

  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.get_value() == value_to_remove:
      self.head_node = self.head_node.get_next_node()
    else:
      while current_node:
        current_next_node = current_node.get_next_node()
        if current_next_node.get_value() == value_to_remove:
          current_node.set_next_node(current_next_node.get_next_node())
          current_node = None
        else:
          current_node = current_next_node

  def remove_all_nodes(self, value_to_remove):
    while self.head_node.get_value() == value_to_remove:
      self.head_node = self.head_node.get_next_node()
    current_node = self.head_node
    while current_node.get_next_node() != None:
      next_node = current_node.get_next_node()
      if next_node.get_value() == value_to_remove:
        current_node.set_next_node(next_node.get_next_node())
      else:
        current_node = next_node

  def remove_index(self, index_to_remove):
    current_node = self.head_node
    if index_to_remove == 0:
      self.head_node = self.head_node.get_next_node()
    else:
      index_count = 1
      current_node = self.head_node
      next_node = current_node.get_next_node()
      if index_count == index_to_remove:
        current_node.set_next_node(next_node.get_next_node())
      else:
        current_node = next_node
        index_count += 1

ll = LinkedList(7)
ll.insert_beginning(8)
ll.insert_beginning(9)
ll.insert_beginning(10)
ll.insert_beginning(11)
ll.insert_beginning(12)
print("Try stringify_list:")
print(ll.stringify_list())
# print(ll.get_head_node().get_value())

print("Try iterating through the list:")
for node in ll:
  print(node)

ll2 = LinkedList()
ll2.insert_beginning(0)
ll2.insert_beginning(1)
ll2.insert_beginning(2)
ll2.insert_beginning(3)
ll2.insert_beginning(4)
ll2.insert_beginning(5)
print("\nA list instantiated without value input (defaulted to None):")
print(ll2.stringify_list())

print("Try iterating through the list and updating None to a new value:")
for node in ll2:
  print("Node:")
  print(node)
  if node.get_value() == None:
    node.update_value([1, 2])
    print("Updated to:")
    print(node)

print("\nCheck if the value update was succesful with stringify_list:")
print(ll2.stringify_list())
