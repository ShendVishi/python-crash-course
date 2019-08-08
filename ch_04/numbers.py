# for value in range(1,5):
#     print(value)

numbers = list(range(1,6))
print(numbers)


#even numbers between 1 (actually 2) and 10
even_numbers= list(range(2,11,2))
print("Even numbers between 1 and 10: " + str(even_numbers))

#square numbers
squares = []
for value in range(1,11):
    #square = value**2
    #squares.append(square)
    squares.append(value**2)
print("Squares of numbers 1 to 10: " + str(squares))

#a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]

print("Numbers: " + str(digits))
print("Minimum: " + str(min(digits)))
print("Maximum: " + str(max(digits)))
print("Sum: " + str(sum(digits)))

#list comprehensions
squares = [value**2 for value in range(1,11)]
print("Squares using list comprehension: " + str(squares))

#count to twenty
for value in range(1,21):
    print(value)
print("End of counting to three")

#one million
# numbers = []
# for value in range(1,1000001):
#     numbers.append(value)
#      print(value)
numbers = [value for value in range(1,1000001)]
print("Min: " + str(min(numbers)))
print("Min: " + str(max(numbers)))
print("Sum: " + str(sum(numbers)))

#odd numbers
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)
print("End of odd numbers\n")
#threes
multiples_of_three = [value*3 for value in range(1,31)]
for multiple in multiples_of_three:
    print(multiple)
print("End of multiples of 3\n")

cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)
print("End of cubes")