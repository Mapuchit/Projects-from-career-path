 ## Trees project
 ## Choose Your Own Adventure: Wilderness Escape

'''Our users get a unique story experience by picking the next chapter of their adventure.'''
 ## use the tree data structure to keep track of the different paths a user may choose

## Our Story Begins
print("Once upon a time…")

######
# TREENODE CLASS
# it will keep track of 1. a portion of the story, 2. the choices a user can make to progress in the story
class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

## Adding Chapters
  def add_child(self, node):
    # each node in the tree is a piece of the story
    # there are multiple paths a user can take
    self.choices.append(node)

## Our Story So Far
  def traverse(self):
    # a variable that will track the current portion of the story
    story_node = self
    print(story_node.story_piece)
    # we want to take user input and progress through the story as long as there are story choices remaining
    while story_node.choices != []:
      # prompt the user for a choice
      choice = input("Enter 1 or 2 to continue the story: ")
      # check if the choice is not invalid
      # we check for string type because we collected input from the terminal
      if choice not in ["1", "2"]:
        # let user know
        print("Please type 1 or 2 to choose.")
      # if the choice is valid
      else:
        # convert the string choice to an int so we can use it as an index
        # the indices in story_node.choices start with 0 not 1 so we need to substract 1 to get the right index
        chosen_index = int(choice) - 1
        # get the appropriate child node using the index
        chosen_child = story_node.choices[chosen_index]
        # this is now our current portion of the story
        # display it to the user
        print(chosen_child.story_piece)
        # update the story_node to the current piece so that we can start the while loop again and continue the story
        story_node = chosen_child
######

######
# VARIABLES FOR TREE
# this is the root of our tree, all stories will begin from this node
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1 ) Roar back!
2 ) Run to the left...
""")

## adding more pieces of the story

# a choice for the middle of the story
choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")
# another choice for the middle of the story
choice_b = TreeNode("""
You come across a clearing full of flowers.
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

# adding a pieces to the story to allow several possible continuations, stored in story_root.choices
story_root.add_child(choice_a)
story_root.add_child(choice_b)

## The Final Chapter

# create the child nodes for choice_a
choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

# adding the children to choice_a
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

# create the child nodes for choice_b
choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")
choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
# adding the children to choice_a
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
######

######
# TESTING AREA
# test out that our root story works
# print(story_root.story_piece)

## Taking Input From the User
# we want to make the story interactive
# user_choice = input("What is your name? ")
# whatever the user types in as a response to the prompt will be assigned to the variable user_choice
# print(user_choice)
######

# We use the traverse method run the game and go through the chapters of the story
story_root.traverse()
