 ## SkyRoute: A Graph Search Program

'''
Vancouver’s public metro system has asked you to help create a program to help commuters get from one landmark to another.
You’ll be building out “SkyRoute” a routing tool that uses breadth-first search, depth-first search, and Python dictionaries to accomplish this feat.
For the purposes of this project, you can assume that it takes the same amount of time to get from each station to each of its connected neighboring stations.
'''

# import functions and dictionaries
from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices


# Build the program:


# define a variable that contains a string that joins all of the landmarks together,
# each with its corresponding letter of the alphabet from landmark_choices on a new line

landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)


## we want to modify the existing system to account for station closings
## create a list to store the closed stations
stations_under_construction = []


# define a greet() function that prints a greeting and informs the user on the programs purpose
# it also prints the list of landmarks and their corresponding letters for the user to see

def greet():
  print("Hi there and welcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)


# define a function that will contain our full program

def skyroute():
  # it starts with greeting the user
  greet()
  # call the wrapper function
  new_route()
  # finish the search
  goodbye()


# define some helper functions


# a function that will handle setting the selected origin and destination points

def set_start_and_end(start_point, end_point):

  # if the start_point has been set already
  if start_point is not None:
    # we already have an origin and destination, but the user wants to make a change
    # collect input from the user
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    # we handle the input
    if change_point == "b":
      # collect and reset both start and end points
      start_point = get_start()
      end_point = get_end()
    elif change_point == "o":
      # collect and reset only the start point
      start_point = get_start()
    elif change_point == "d":
      # collect and reset only the end point
      end_point = get_end()
    else:
      # to handle cases in which the user typed some other value
      print("Oops, that isn't 'o', 'd', or 'b'...")
      # recursively call set_start_and_end() on start_point and end_point so that the user has a chance to try again
      set_start_and_end(start_point, end_point)

  # if the start_point has not been set
  else:
    # collect start and end points using the helper functions
    start_point = get_start()
    end_point = get_end()

  # return both start and end points
  return start_point, end_point


# a function that will be used to request an origin from the user

def get_start():
  # collect user input
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  # make sure the user entered a real landmark name
  if start_point_letter in landmark_choices.keys():
    # if it's a valid choice we can set start_point using the landmark_choices dictionary
    start_point = landmark_choices[start_point_letter]
    # the function returns the start_point
    return start_point
  else:
    # if the choice is not valid
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    # return a recursive call so that the user gets a chance to get it right
    return get_start()


# a function that will be used to request a destination from the user

def get_end():
  # collect user input
  end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
  # make sure the user entered a real landmark name
  if end_point_letter in landmark_choices.keys():
    # if it's a valid choice we can set end_point using the landmark_choices dictionary
    end_point = landmark_choices[end_point_letter]
    # the function returns the end_point
    return end_point
  else:
    # if the choice is not valid
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    # return a recursive call so that the user gets a chance to get it right
    return get_end()


# build a wrapper function for the bulk of the program that we can use to:
# A: get and set the origin and destination
# B: call search to get the recommended route
# C: allow users to search for another route

# the function will take start_point and end_point as parameters with default value None
# because start and end may need to be defined for the first time or redefined upon subsequent new_route() calls

def new_route(start_point = None, end_point = None):

  # A: we set start and end using our previously defined function
  start_point, end_point = set_start_and_end(start_point, end_point)

  # B: find the shortest route between start and end
  shortest_route = get_route(start_point, end_point)

  ## accounting for station closures: with certain stations closed, some routes will cease to exist
  ## we need to check if shortest_route exists
  if shortest_route:
    # shortest_route is a list, so we covert it into a more user friendly format
    # a string that has each station from shortest_route on a new line
    shortest_route_string = '\n'.join(shortest_route)
    # print the shortest route for the user to see
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  else:
    ## if shortest_route doesn't exist it means there is not path between the two landmarks
    print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))

  # C: collect user input on whether they want to see other routes
  again = input("Would you like to see another route? Enter y/n: ")
  # if they do:
  if again == "y":
    # it might be helpful for the user to see the list of landmarks again
    show_landmarks()
    # make a recursive call the new_route()
    # our function will loop as long as our user wants to look up new directions
    new_route(start_point, end_point)


# a helper function to show all the landmark to the user

def show_landmarks():
  # ask the user if they want to see the list of landmarks again
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
  # if yes
  if see_landmarks == "y":
    # use our previously created landmark_string
    print(landmark_string)


# a function that uses breadth-first search to find the best route between selected points
# start_point and end_point are landmarks, not metro stations and some landmarks have more than one metro station
# in order to get the metro stations closest to to each landmark, we need to access them through the vc_landmarks dictionary

def get_route(start_point, end_point):
  # we grab the sets of stations connected to the start_point and end_point landmarks
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  # because some landmarks have more than one station, there is sometimes more than one route between landmarks
  # it’s our job to collect ALL of the shortest routes between stations and then compare them based on path length
  # to collect our shortest routes for comparison, create an empty list
  routes = []
  # we loop through each station in start_stations
  for start_station in start_stations:
    # and each station in end_stations
    for end_station in end_stations:

      ## add changes to accommodate our new updated_metro graph if there are stations under construction
      ## if stations_under_construction isn't empty we use the updated metro graph returned with the helper function
      ## if there are no stations_under_construction we can keep using the original graph
      metro_system = get_active_stations() if stations_under_construction else vc_metro

      ## if there are stations_under_construction it means we might not find a route at all
      if stations_under_construction:
        ## so it is worth to check if a route even exists using the dfs() function
        possible_route = dfs(metro_system, start_station, end_station)
        ## if there is no possible_route we return None, we need this step because
        ## then shortest_route will be None in new_route() and we have some control flow set up to handle that condition
        if not possible_route:
          return None

      ## update the graph used to metro_system so that we can get the shortest route for whichever metro graph is currently in place
      # we call bfs() on each combination of start and end station to find all the shortest routes
      route = bfs(metro_system, start_station, end_station)
      # check if a route exists between the two stations looked at
      if route is not None:
        # the route returned from bfs() is a list that represents the path
        # add this new shortest route to the routes list
        routes.append(route)

  # after the loops finished we have all the shortest route options saved in routes
  # we can now get our shortest route from the list based on list length
  shortest_route = min(routes, key = len)
  return shortest_route


# a helper function to finish up the search experience
def goodbye():
  print("Thanks for using SkyRoute!")


## we create a modified version of the vc_metro graph to work with when there are any stations under construction
## define a function that automatically generates an updated graph based on what is added to the stations_under_construction list

def get_active_stations():
  # we copy the stations dictionary
  updated_metro = vc_metro
  # in order to create the updated system, we need to remove any connections to and from the closed stations

  # we loop through the list of stations_under_construction
  for station_under_construction in stations_under_construction:
    # loop through all keys and values in the vc_metro dictionary
    for current_station, neighboring_stations in vc_metro.items():
      # check if the current station is not the station under construction we are looking at in the outer loop
      if station_under_construction != current_station:
        # if it’s not, we want to remove any of its connecting stations that are under construction
        # we add the current station to the new dictionary with a value of its current set of stations
        # minus a set of the stations_under_construction
        updated_metro[current_station] = neighboring_stations - set(stations_under_construction)
      else:
        # if the current_station is the station_under_construction
        # we add it to the new dictionary with a value of a set with an empty list that means no connections to and from this station
        # this will allow us to keep the current landmarks dictionary but prevent any connections from the stations that are under repair
        updated_metro[current_station] = set([])

  # when the loops are finished the new graph is ready
  return updated_metro




# testing
# print(set_start_and_end(None, None))
# prints (None, None) until get_end() and get_start() are not completed
# after the helper functions have been completed
# ('Lions Gate Bridge', 'Kitsilano Beach') for start_point = "i", end_point = "r"
# print(get_route('Canada Place', 'Central Park'))
# ['Burrard', 'Granville', 'Stadium-Chinatown', 'Main Street-Science World', 'Commercial-Broadway', 'Nanaimo', '29th Avenue', 'Joyce-Collingwood', 'Patterson']
# print(get_active_stations()) # 'Aberdeen': set() if 'Aberdeen' is added to stations_under_construction list
skyroute()
