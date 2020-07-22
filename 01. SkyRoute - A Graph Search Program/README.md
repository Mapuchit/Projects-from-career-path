# SkyRoute - A Graph Search Program
> Help commuters in Vancouver metro to get from one landmark to another in the city.
> Account for stations being under construction.

## General info
Uses breadth-first search, depth-first search, and Python dictionaries to build a navigation program.

## Technologies
* Python 3.7.6
* Git Bash 2.27.0
* Atom v1.49.0
* Windows 10 Pro

## Features
* The metro map with stations and their connections represented by a graph.
* Greet user and display list of landmarks to choose from.
  * Each landmark is identified by a letter of the alphabet to make choice quicker.
* Option to set start and destination to the journey, separately or both at the same time.
  * Start and destination are chosen from the landmarks list using the alphabetical code.
  * Check if the choice is valid and display message if not.
* Find the shortest route between the two chosen landmarks using breadth-first search.
  * Access metro stations closest to chosen landmarks using a dictionary.
  * Find all possible routes between the two landmarks and pick the shortest one.
  * Display for the user all the stations in the shortest route.
* Allow users to search for another route until they wish to exit the program.
  * Show list of landmarks again for user for ease of choice.
  * Recursive call to choosing landmarks and finding route.
* Handle stations under construction.
  * Before searching for a route the system checks if there are any stations under construction.
  * Generate a new metro map (graph) that removes all connections to stations under construction, leaving only the active stations.
  * Check if there is a route available at all using a depth-first search.
  * Display message if there is no route available due to construction.
* Say goodbye to user when they decide to finish using the program.

To-do list:
* What happens if the user enters the same station for their origin and destination?
* Create a user interface for employees to update the stations under construction.

## Status
Project is: _in progress_

## Inspiration
This is a guided project that practices graph search algorithms from the Computer Science Carreer Path on [Codecademy](https://www.codecademy.com/learn).
