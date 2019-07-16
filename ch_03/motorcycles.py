motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

#append element at the end
motorcycles.append('ducati')
print(motorcycles)

#empty the list
motorcycles = []
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.append('yamaha')
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

#insert element at specified position
motorcycles.insert(0, 'ducati')
print(motorcycles)

#remove element given the index (position)
del motorcycles[0]
print(motorcycles)

#pop (remove and return)
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#pop items given the position
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#remove by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)