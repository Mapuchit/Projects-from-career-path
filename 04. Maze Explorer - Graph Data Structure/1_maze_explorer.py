 ## Graphs project
 ## Maze Explorer

''' Using the graph data structure we model the layout of archeological ruins containing valuable artifacts.
We map the optimal path through the chambers to find these artifacts before our torch burns out.'''

 ## Gearing up!

# import classes
from maze_graph import Graph, build_graph
from maze_vertex import Vertex

# create the excavation site Graph instance
excavation_site = build_graph() # prints MAZE LAYOUT

 ## Exploring the Maze
# we call explore() to run the game
excavation_site.explore()
