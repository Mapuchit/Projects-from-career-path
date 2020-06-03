 ## Dictionaries project
 ## Abruptly Goblins

'''
Your beloved clientele want to organize a game night at your comics store! Create a system for organizing and tracking gamer’s availability.
Programmatically figure out the best day to host a game night and send out emails to your attendees to let them know when to come.
'''

## Introduction - adding gamers

# a list of people who are attending game night.
gamers = []
# a function to add gamers to the list
def add_gamer(gamer, gamers_list):
    if "name" in gamer.keys() and "availability" in gamer.keys():
        gamers_list.append(gamer)

# try it out
gamers = []
kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
print(gamers)

# add more gamers
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

## Finding the perfect availability

# a function to create a dictionary with the days of the week as keys and 0s for values
def build_daily_frequency_table():
    freq_table = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
    return freq_table

count_availability = build_daily_frequency_table()
print(count_availability)

# a function to count the number of people available each night of the week
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1

# calculate
calculate_availability(gamers, count_availability)
print(count_availability)

# a function to find the night of the week with the most people available
def find_best_night(availability_table):
    max_gamers = max(availability_table.values())
    for key in availability_table.keys():
        if availability_table[key] == max_gamers:
            return key

# find the best night
game_night = find_best_night(count_availability)
print(game_night)

# create a list of the people available on that night
def available_on_night(gamers_list, day):
    available_gamers = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            available_gamers.append(gamer["name"])
    return available_gamers

attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

## Generating an E-mail for the Participants

# create a default email
form_email = "Dear {name}! The game night for {game} will be held on {day_of_week}."

# print out the individual emails to send using a function
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer, game = game, day_of_week = day))

send_email(attending_game_night, game_night, "Abruptly Goblins!")

## Afterward - for those who cannot attend

# a list of people who are not able to attend the chosen game night
unable_to_attend_best_night = []
for gamer in gamers:
    if gamer["name"] not in attending_game_night:
        unable_to_attend_best_night.append(gamer)

# calculate the second best night
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
print(second_night)

# send out an email to notify everyone who can attend the second night (regardless whether they can attend the first night or not)
available_second_game_night = available_on_night(gamers, second_night)
print(available_second_game_night)

send_email(available_second_game_night, second_night, "Abruptly Goblins!")
