players = ['charles', 'martina', 'michael', 'florence', 'eli']
#items 0(first) to 2
print(players[0:3])
#items 0 to 3
print(players[:4])
#items 2 to the end
print(players[2:])
#last three items
print(players[-3:])

#print first three players
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

