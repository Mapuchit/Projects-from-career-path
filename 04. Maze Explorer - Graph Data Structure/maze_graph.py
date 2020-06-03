## a Graph class partly provided in the lesson

from maze_vertex import Vertex

class Graph:
  def __init__(self):
    # dictionary with data {key(room name): value(vertex object)}
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    self.graph_dict[to_node.value].add_edge(from_node.value, weight)


  def explore(self):
    print("Exploring the graph....\n")

 ## Exploring the Maze
    # we start from the entrance
    current_room = "entrance"
    # and track the path we take
    path_total = 0
    print("\nStarting off at the {0}.\n".format(current_room))
    # we keep navitgating until we find the treasure room
    while current_room is not "treasure room":
      # we first retrieve all the data of the current room that is saved in the graph dictionary
      # node = vertex object entrance
      node = self.graph_dict[current_room]
      # to check the adjacent rooms
      # we iterate through the dictionary items of the node to get the keys (adjacent rooms) and values (weight)
      for connected_room, weight in node.edges.items():
        # we show the user all the choices of rooms to go to and their costs
        # we will identify the rooms by their first letters
        key = connected_room[0]
        print("enter {0} for {1}: {2} cost".format(key, connected_room, weight))
      # after we printed all the choices for the current room we get the user's input
      # the valid choices are a list of the first letters of the adjacent rooms
      valid_choices = [connected_room[0] for connected_room in node.edges.keys()]
      print("\nYou have accumulated: {0} cost".format(path_total))
      choice = input("\nWhich room do you move to? ")
      # in case the user entered an invalid choice
      if choice not in valid_choices:
        print("please select from these letters: {0}".format(valid_choices))
      # if the choice is valid
      else:
        # match the input letter to the room
        for connected_room in node.edges.keys():
          # if there is a match
          if connected_room.startswith(choice):
            # we update the current room we are in
            current_room = connected_room
            # we update the path total with the weight
            path_total += node.edges[connected_room]
        # confirm the choice for the user
        print("\n*** You have chosen: {0} ***\n".format(current_room))
    # when the while loop is finished it means we found the treasure room
    print("Made it to the treasure room with {0} cost".format(path_total))


  def print_map(self):
    print("\nMAZE LAYOUT\n")
    for node_key in self.graph_dict:
      print("{0} connected to...".format(node_key))
      node = self.graph_dict[node_key]
      for adjacent_node, weight in node.edges.items():
        print("=> {0}: cost is {1}".format(adjacent_node, weight))
      print("")
    print("")


def build_graph():
  graph = Graph()

 ## Entering the maze
  # make vertices for each room in the maze
  entrance = Vertex("entrance")
  ante_chamber = Vertex("ante-chamber")
  kings_room = Vertex("king's room")
  # add rooms to the graph
  graph.add_vertex(entrance)
  graph.add_vertex(ante_chamber)
  graph.add_vertex(kings_room)

  # add edges between rooms
  graph.add_edge(entrance, ante_chamber, 7)
  graph.add_edge(entrance, kings_room, 3)
  # we discovered a passage between the two first rooms
  graph.add_edge(kings_room, ante_chamber, 1)

 ## Mapping the maze
  # we discover two more rooms
  grand_gallery = Vertex("grand gallery")
  graph.add_vertex(grand_gallery)
  graph.add_edge(grand_gallery, ante_chamber, 2)
  graph.add_edge(grand_gallery, kings_room, 2)

  treasure_room = Vertex("treasure room")
  graph.add_vertex(treasure_room)
  graph.add_edge(treasure_room, ante_chamber, 6)
  graph.add_edge(treasure_room, grand_gallery, 4)

  # print the graph layout
  graph.print_map()
  return graph
