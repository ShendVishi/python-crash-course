current_users = ['admin', 'shend', 'user2', 'username5', 'anotheruser']
new_users = ['newuser1', 'john', 'shend', 'joe', 'admin']

for new_user in new_users:
    if new_user in current_users:
        print(new_user + " already exists. Please pick another username!")
    else:
        print(new_user + " is available.")