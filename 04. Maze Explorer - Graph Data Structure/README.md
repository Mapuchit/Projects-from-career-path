# Maze Explorer - Graph Data Structure
> A game where we need to find a treasure in the hidden chamber within mysterious ruins. 
> Entering each new chamber has a cost which adds up. The goal is to find the cheapest (easiest) route to the treasue.

## General info
Use the graph data structure to create and navigate the map of the ruins.

## Technologies
* Python 3.7.6 
* Git Bash 2.27.0
* Atom v1.49.0
* Windows 10 Pro

## Features
* A Vertex class to represent the chambers and keep track of how the different chambers are connected to each other.
  * The cost of moving to a new chamber is modelled by weighted edges between the vertices.
* A Graph class to represent the maze inside the ruins.
  * Method to build a new graph (maze) by adding new chambers (vertices) and passages (edges).
  * Option to print the map of the maze by displaying all the chambers and how they are connected.
* Explore the maze by navigating through the graph.
  * Display the choices from current location. The user can see which chambers are connected and what is the cost of entering each.
  * Display how much cost the user has accumulated until current choice.
  * Check if the user choice is a valid input.
  * Increment the cost counter and display result at the end of the game.

## Status
Project is: _finished_

## Inspiration
This is a guided project that practices graph data structure from the Computer Science Carreer Path on [Codecademy](https://www.codecademy.com/learn).
