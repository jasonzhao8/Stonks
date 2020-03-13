# Jason Zhao
# RPG Dictionary assignment
# March 12 2020

# Playable characters/ the users characters.
user = {'PlayerName': 'USERINPUTNAME'}
cpname = {'Company Name': 'USERCOMPANYNAME'}
character = user.get('PlayerName', 'Company Name')
umessage = user['PlayerName'].title()
cpmessage = cpname['Company Name'].title()
print("You are " f"{umessage}"", the owner of "f"{cpmessage}.")

# NPC/ OfficeEmployees.
employees = {
    'emp1': 'Bob', 'ef': '30',
    'emp2': 'Joe', 'ef': '40',
    'emp3': 'Arnold', 'ef': '20',
    }

empstate1 = employees['emp1'].title(), employees['ef'].title()
empstate2 = employees['emp2'].title(), employees['ef'].title()
empstate3 = employees['emp3'].title(), employees['ef'].title()

print("Your current employee list:")
print(f"{empstate1}""% efficiency")
print(f"{empstate2}""% efficiency")
print(f"{empstate3}""% efficiency")

# The users inventory. remains stagnant.
inventory = {'Slot1': 'Efficiency Increase',
             'Slot2': 'GuideBook',
             'Slot3': 'Cellphone',
             }

message1 = inventory['Slot1'].title()
message2 = inventory['Slot2'].title()
message3 = inventory['Slot3'].title()

print("Your Inventory:")
print("In slot1 you have "f"{message1}")
print("In slot2 you have "f"{message2}")
print("In slot3 you have "f"{message3}")

# Location (5x1). This code creates the building layout including 5 rooms.
buildingnest = {
                'washroom': {'sink': 'to wash hands',
                             'toilet': 'to use'},
                'OfficeEmployees':
                            {'To manage employees List':
                             'Employee cubicles'},
                }
room1 = buildingnest['washroom']
room2 = buildingnest['OfficeEmployees']

print('Building Floorplan (left to right):')
print("Washroom: "f"{room1}")
print("Employees office: " f"{room2}")

building = {
    'Lobby': 'To view your stats',
    'BreakRoom': 'For Board meetings',
    'OfficeMain': 'Your office'
    }
room3 = building['Lobby']
room4 = building['BreakRoom']
room5 = building['OfficeMain']

print("Lobby: " f"{room3}")
print("BreakRoom: " f"{room4}")
print("Your Office: " f"{room5}")
