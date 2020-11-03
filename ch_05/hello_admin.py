users = ['admin', 'shend', 'user2', 'username5', 'anotheruser']

if len(users) == 0:
    print("We need to find some users")

for user in users:
    if user == 'admin':
        print("Hello " + user + ", would you like too see a status report?")
    else:
        print("Hello " + user + "!")