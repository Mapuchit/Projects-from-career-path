 ## Files programming project
 ## Hacking The Fender - working with text files CSV to retrieve, manipulate, obscure, and create data

'''
The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own.
Your mission, should you choose to accept it, is threefold.
1. You must acquire access to The Fender‘s systems.
2. You must update his "passwords.txt" file to scramble the secret data.
3. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.
'''

 ## Reading In The Passwords
'''
write a program that will read in the compromised usernames and passwords that are stored in a file called "passwords.csv"
'''

# import the csv module
import csv

# a list of users whose passwords have been compromised
compromised_users = []

# open the passwords.csv file
with open("passwords.csv") as password_file:
  # to read the csv prase it to a dictionary
  password_csv = csv.DictReader(password_file)
  # iterate through the lines in the csv
  for row in password_csv:
    # save each separate row\dict
    password_row = row
    # print the username of the person whose password was compromised
    # print(password_row['Username'])
    # we can see the list of compromised user names when the code is run
    # add each username to the list of compromised_users
    compromised_users.append(password_row['Username'])

# we can exit the "with" block and thus close the passwords.csv file after we retreived the compromised usernames

# create a new file to save the compromised usernames
with open("compromised_users.txt", "w") as compromised_user_file:
  # iterate over the compromised users list
  for user in compromised_users:
    # write each username in our new file
    compromised_user_file.write(user + "\n")

# we can close the compromised_users.txt
# check if the writing was successful
print("The list of compromised usernames:")

with open("compromised_users.txt") as compromised_user_file:
  user_list = compromised_user_file.read()
  print(user_list)

 ## Notifying the Boss
'''
Your boss needs to know that you were successful in retrieving that compromised data.
We’ll need to send him an encoded message over the internet. Let’s use JSON to do that.
'''

import json

 # create a json file
with open("boss_message.json", "w") as boss_message:
  # create a Python dict object to contain the message
  boss_message_dict = {
    "recipient": "The Boss", "message": "Mission Success"
    }
  # write the message to the json file
  json.dump(boss_message_dict, boss_message)

# check the message
with open("boss_message.json") as boss_message_json:
  message = json.load(boss_message_json)
  print(message)

 ## Scrambling the Password
'''
Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv" file completely.
'''

# open a new passwords file in write mode
with open("new_passwords.csv", "w") as new_passwords_obj:
  # save Slash Null's signature
  slash_null_sig = '''
 _  _     ___   __  ____
/ )( \\   / __) /  \\(_  _)
) \\/ (  ( (_ \\(  O ) )(
\\____/   \\___/ \\__/ (__)
 _  _   __    ___  __ _  ____  ____
/ )( \\ / _\\  / __)(  / )(  __)(    \\
) __ (/    \\( (__  )  (  ) _)  ) D (
\\_)(_/\\_/\\_/ \\___)(__\\_)(____)(____/
        ____  __     __   ____  _  _
 ___   / ___)(  )   / _\ / ___)/ )( \\
(___)  \\___ \\/ (_/\\/    \\\\___ \\) __ (
       (____/\\____/\\_/\\_/(____/\\_)(_/
 __ _  _  _  __    __
(  ( \\/ )( \\(  )  (  )
/    /) \\/ (/ (_/\\/ (_/\\
\\_)__)\\____/\\____/\\____/
  '''
  # write the signature into the new passwords file, this will replace the old file to make The Fender to think Slash Null was behind this attack
  new_passwords_obj.write(slash_null_sig)

# print it out
with open("new_passwords.csv") as new_passwords:
    contents = new_passwords.read()
    print(contents)
