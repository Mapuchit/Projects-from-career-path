 ## Dictionaries project
 ## Scrabble - processing data from a group of friends playing scrabble, using dictionaries to organize players, words, and points

## Build the Point Dictionary

# combining the lists letters and points into a dictionary that maps a letter to it's point value
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# a dictionary that has the elements of letters as the keys and the elements of points as the values
letter_to_points = {letter : point for letter, point in zip(letters, points)}

# adding another entry to the dictionary to account for blank tiles
letter_to_points[" "] = 0
print("How many points each character gives you:")
print(letter_to_points)

# a function that takes in a word and returns how many points that word is worth
# can handle both upper and lower case characters
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total

# testing the function
brownie_points = score_word("BROWNIE")
print("The word \"BROWNIE\" is worth " + str(brownie_points) + " points.") # prints 15

## Score a Game

# a dictionary that maps players to a list of the words they have played
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
print("The list of words played by each player this far:")
print(player_to_words)

# A dictionary that maps players to their total points in the game
player_to_points = {}
# summing up the points for all the letters in each word for each player
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# the current standings for this game
print("The game standings this far:")
print(player_to_points)

# a function that takes in a player and a word, and adds that word to the list of words they’ve played
def play_word(player, word):
  player_to_words[player] += [word]

# a new word played by "player1"
play_word("player1", "BLABLA")
print("An updated list of words played, after player1 played the word \"BLABLA\".")
print(player_to_words)

# turning the nested loops into a function that can be called any time a word is played
def update_point_totals(player, word):
  play_word(player, word)
  print("The word \"" + word + "\" is worth " + str(score_word(word)) + " points for " + player + ".")
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print("The updated points tables is:")
  print(player_to_points)
  return player_to_points

# "wordNerd" played the word "HOORAY"
update_point_totals("wordNerd", "HOORAY")

# "Lexi Con" played the word "shalala"
update_point_totals("Lexi Con", "shalala")

# "Prof Reader" played the word "tertyeget"
update_point_totals("Prof Reader", "tertyeget")
