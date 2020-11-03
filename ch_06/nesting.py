aliens = []

for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }

    aliens.append(new_alien)

# modify the first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'medium'
        alien['points'] = 10

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens is {len(aliens)}.")