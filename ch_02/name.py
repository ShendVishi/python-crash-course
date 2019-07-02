name = "ada lovelace"

print(name.title())

print(name.upper())

print(name.lower())

#String concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)

#Whitespace
#\t for tab, \n for newline
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

#Stripping Whitespace
favorite_language = 'python '
print(favorite_language)

favorite_language.rstrip() #doesn't change the string
print(favorite_language)

favorite_language = favorite_language.rstrip() #changes the string permanently
print(favorite_language)

favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())