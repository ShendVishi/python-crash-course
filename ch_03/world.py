places_to_visit = ['Thailand', 'India', 'Japan', 'Mexico', 'Argentina', 'Iceland', 'Portugal']
print("Original list:")
print(places_to_visit)
#sort the list without modyfing it
print("\nSorted:")
print(sorted(places_to_visit))

#the list still keeps the original order
print("The original list is still the same:\n")
print(places_to_visit)

#reverse alphabetical order without changing the order of the original list
print("\nReverse alphabetical order:")
print(sorted(places_to_visit, reverse=True))

#print the original
print("\nThe original list is still the same:")
print(places_to_visit)

#change order
places_to_visit.reverse()
print("\nOrder has changed (reverse):")
print(places_to_visit)

#sort
print("\nSorted:")
places_to_visit.sort()
print(places_to_visit)

#sort in reverse alphabetical order
places_to_visit.sort(reverse=True)
print("\nSorted in reverse alphabetical order:")
print(places_to_visit)
