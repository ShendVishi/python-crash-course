guests =  ['Barack Obama', 'Alexander the Great', 'Robin Williams', 'Skanderbeg']
print("Hi " + guests[0] + "! I would like to invite you to dinner :)")
print("Hi " + guests[1] + "! I would like to invite you to dinner :)")
print("Hi " + guests[2] + "! I would like to invite you to dinner :)")
print("Hi " + guests[3] + "! I would like to invite you to dinner :)")

print(guests[1] + " can't make it. :(")
guests[1] = 'Beyonce'

print("Hi " + guests[0] + "! I would like to invite you to dinner :)")
print("Hi " + guests[1] + "! I would like to invite you to dinner :)")
print("Hi " + guests[2] + "! I would like to invite you to dinner :)")
print("Hi " + guests[3] + "! I would like to invite you to dinner :)")

print("I found a bigger table. More people are coming. Yaay!")

guests.insert(0, 'Franz Kafka')
guests.insert(3, 'Gabriel Garcia Marquez')
guests.append('Dave Chappelle')

print("Hi " + guests[0] + "! I would like to invite you to dinner :)")
print("Hi " + guests[1] + "! I would like to invite you to dinner :)")
print("Hi " + guests[2] + "! I would like to invite you to dinner :)")
print("Hi " + guests[3] + "! I would like to invite you to dinner :)")
print("Hi " + guests[4] + "! I would like to invite you to dinner :)")
print("Hi " + guests[5] + "! I would like to invite you to dinner :)")
print("Hi " + guests[6] + "! I would like to invite you to dinner :)")
print('Number of guests: ' + str(len(guests)))
print("Sorry! I can only invite two people for dinner.")

print(guests.pop() + ', you are no longer invited. Sorry!')
print(guests.pop() + ', you are no longer invited. Sorry!')
print(guests.pop() + ', you are no longer invited. Sorry!')
print(guests.pop() + ', you are no longer invited. Sorry!')
print(guests.pop() + ', you are no longer invited. Sorry!')

print("Hi " + guests[0] + "! I would like to invite you to dinner :)")
print("Hi " + guests[1] + "! I would like to invite you to dinner :)")

del guests[1]
del guests[0]

print(guests)

print('Number of guests: ' + str(len(guests)))

#index error
#print(guests[2])