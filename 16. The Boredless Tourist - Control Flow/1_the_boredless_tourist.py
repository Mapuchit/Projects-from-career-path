 ## Project: "The Boredless Tourist" - Build a Tourism Recommendation Engine

# list of available destinations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

# name of traveler, current location, interests
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# gets the index of a destination from the list of available destinations
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# try get_destination_index function with different inputs
def print_destination_index(destination):
  print("The destination index of " + destination + " is " + str(get_destination_index(destination)))

destination = "Los Angeles, USA"
print_destination_index(destination) # 2
destination = "Paris, France"
print_destination_index(destination) # 0
#destination = "Hyderabad, India"
#print_destination_index(destination) # raises ValueError error because destination is not on the list

# gets traveler location from traveler info and matches it to index in destinations list
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print("The destination index of the test traveler is " + str(test_destination_index)) # 1

# create a list of attractions for each of the 5 destination in our destinations list
# 5 empty sublists in a list
attractions = [[], [], [], [], []]
# or using a loop
attractions1 = []
for destination in destinations:
  attractions1.append([])
# or using list comprehension
attractions2 = [[] for destination in destinations]

print(attractions)
print(attractions1)
print(attractions2)

# adds an attraction to a destination by saving it to the appropriate sublist in the attractions list, prints error message if destination is not on list
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    print("Destination not on list!")
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

# adds attractions as list with a sublist, the list is the name of the attraction and the sublist is a tag with information
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions) # places attraction at index[2] of attractions list to match the index of destination Los Angeles, USA

# adding more attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# matching the travelers interests with the attractions in the city
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = possible_attraction[1]
    for interest in interests:
      for tag in attraction_tags:
        if tag == interest:
          attractions_with_interest.append(possible_attraction[0])
      # if interest in attraction_tags: (without adding another loop)
        # attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

# trying the function find_attractions
la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts) # prints 'LACMA'

# connecting people with the attraction they want to see, according to their destination and interests
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination
  for attraction in traveler_attractions:
    interests_string += ": " + attraction
  return interests_string

# trying the function
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
erin_china = get_attractions_for_traveler(test_traveler)
print(erin_china)
