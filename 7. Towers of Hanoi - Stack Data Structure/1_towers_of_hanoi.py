 ## Stacks project
 ## Towers of Hanoi - mathematical puzzle with with three stacks and many disks

''' The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.

The game follows three rules:

    1. Only one disk can be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
    3. No disk may be placed on top of a smaller disk. '''

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

## Creating the Stacks

# a list to store our 3 stacks
stacks = []

# three stack instances
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

# append them to the list
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

## Setting up the Game

# create a number of disks corresponding to how many disks the user wants to play with
# input() will print to the terminal
num_disks = int(input("\nHow many disks do you want to play with?\n"))

# we should have at least 3 disks to make the game fun
# message will print if we enter a number less than 3
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

# adding disks with numbers representing the size: Disk 3 is larger than Disk 1 etc.
# we iterate through num_disks backwards, so we handle the largest disk first
for disk in range(num_disks, 0, -1):
  # and push the disks onto the left (initial) stack to be able to start the game
  left_stack.push(disk)

# calculate the number of optimal moves, which is always 2 ** Number of Disks - 1 for towers of hanoi
num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {n} moves".format(n = num_optimal_moves))

## Getting User Input

# create a helper function that prompts users to choose the stack by entering it's first letter
def get_input():
  # a variable containing the list of choices, getting the first letters with the Stack method get_name
  choices = [stack.get_name()[0] for stack in stacks]
  # keep asking the user for input until we get a valid input
  while True:
    # first we print our choices and what the letters mean
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {l} for {n}".format(l = letter, n = name))
    # get the input
    user_input = input("")
    # check is the user made a valid choice
    if user_input in choices:
      # check which stack the user chose
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

## Playing the Game

# we need to keep track of the number of user moves
num_user_moves = 0

# the game ends when the right stack is full so we need to keep going until it's then
while right_stack.get_size() != num_disks:
  # first print our current stacks to see how the game stands
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  # keep asking the user what move they want to make until they make a valid move
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    # checking the validity of the moves
    # we check if the user made an invalid move by trying to move from an empty stack
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    # if the user moves a disk to an empty stack or moves a disk onto a larger disk, that’s a valid move
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      # we take the disk from the origin stack
      disk = from_stack.pop()
      # put in on the destination stack
      to_stack.push(disk)
      # and update the moves counter
      num_user_moves += 1
      break # the inner while loop
    # the only ramining option is if the user tries to move a larger disk onto a smaller disk
    else:
      print("\n\nInvalid Move. Try Again")

# if the outer while loop is no longer running it means the game is finished
print("\n\nYou completed the game in {m} moves, and the optimal number of moves is {o}".format(m = num_user_moves, o = num_optimal_moves))
