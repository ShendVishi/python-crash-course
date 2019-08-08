#define list
magicians = ['alice', 'david','carolina']
#define for loop
for magician in magicians:
    #for every magician in the list of migicians, print the magician's name
    print(magician)

#do more work within a loop
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    #next line is not indented, therefore not inside the loop
print("Thank you, everyone. That was a great magic show!")