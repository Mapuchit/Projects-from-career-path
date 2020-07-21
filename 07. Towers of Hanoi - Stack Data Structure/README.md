# Towers of Hanoi - Stack Data Structure
> Implementation of game using stack data structure in Python.

## General info
Practice stack data structure and Python classes to model the stacks and disks of the Towers of Hanoi game. The description of the game as it appeares in the project:

The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.
The game follows three rules:
  1. Only one disk can be moved at a time.
  2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
  3. No disk may be placed on top of a smaller disk.

## Technologies
* Python 3.7.6 
* Git Bash 2.27.0
* Atom v1.49.0
* Windows 10 Pro

## Features
* A Node class that models the disks on the stacks.
  * Disk size is represented by numbers. Larger disks have greater numbers.
* A Stack class that keeps track of size of the stack and the top item.
  * There is a set limit for how many disks a stack can take.
  * Methods to push a disk to the stack or pop a disk from the top of the stack.
* Ask the user how many disks they want to play with and check if number is greater than 3 to ensure the game is challenging.
* Calculate the smallest number of moves that can solve the game with the chosen number of disks and display this to the user.
* Ask the user to choose a stack to take disks from or put disks into.
* Display current condition of stacks before each move.
* At the end of game display the number of moves the user made has compared with the smallest possible number of moves.

## Status
Project is: _finished_

## Inspiration
This is a guided project that practices stack data structure from the Computer Science Carreer Path on [Codecademy](https://www.codecademy.com/learn).
