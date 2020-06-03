## a Vertex class provided in the lesson

class Vertex:
  def __init__(self, value):
    self.value = value
    # dictionary with data {key(adjacent room name): value(weight)}
    self.edges = {}

  def add_edge(self, adjacent_value, weight = 0):
    self.edges[adjacent_value] = weight

  def get_edges(self):
    return self.edges.keys()
