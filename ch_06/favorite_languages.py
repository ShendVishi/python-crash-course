favorite_languages = {
    'minzah': 'java',
    'shend': 'python',
    'nate': 'javascript'
}

# loop through key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# loop through keys
for name in favorite_languages.keys():
    print(name.title())

# same result as looping through keys
for name in favorite_languages:
    print(name.title())


friends = ['minzah', 'nate']

for name in favorite_languages.keys():
    print(f"Hi, {name.title()}!")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")

# .keys() returns a list of all the keys in a dictionary
if 'edward' not in favorite_languages.keys():
    print("Edward, please take our poll!")

# sorted keys
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

# loop through values of a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# loop through values of a dictionary without repetition
print("The following unique languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


'''
It’s easy to mistake sets for dictionaries because they’re both wrapped in braces.
When you see braces but no key-value pairs, you’re probably looking at a set.
Unlike lists and dictionaries(>=3.7), sets do not retain items in any specific order.
'''
languages = {'python', 'java', 'c', 'java'}
print(languages)