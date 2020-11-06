prompt = "Please enter the name of a city you've been to: "
prompt += "\n(Enter 'quit' when you're done.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"{city.title()} is cool.")