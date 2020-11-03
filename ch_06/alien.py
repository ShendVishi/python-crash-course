alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
#
# print("You just earned " + str(new_points) + " points!")

print(alien_0)

alien_0['x_position'] = 0;
alien_0['y_position'] = 25;
print(alien_0)

# initialize an empty dictionary
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 3
print(alien_1)

# modify a value in a dictionary
print(f"The alien is {alien_1['color']}.")
alien_1['color'] = 'blue'
print(f"The alien is now {alien_1['color']}.")

# move the alien
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points':10}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 3
else:
    x_increment = 5

alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")

# remove key-value pair (permanently)
del alien_0['points']
print(alien_0)

# simple error handling using the get method
points_value = alien_0.get('points', 'No points value assigned.')
print(points_value)