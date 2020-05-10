# Working with parts of the list

# BOF

# initialize our vars
players = [
    'kawhi leonard',
    'russel westbrook',
    'anthony davis',
    'lebron james',
    'steph curry',
    'james harden'
]

# print the list
print('print the list')
print(players)

# slice the list
print('slice the list')
team01 = players[0:3]
team02 = players[3:6]

print('Team 01')
for team_members01 in team01:
    print(team_members01.title())

print('Team 02')
for team_members02 in team02:
    print(team_members02.title())

# EOF
