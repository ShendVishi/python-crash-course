responses = {}

# flag to indicatte polling is active
polling_active = True

while polling_active:
    # name and response
    name = input("\nWhat's your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # store response in the dictionary
    responses[name] = response

    # other responders
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
# polling completed
print("\n--- Poll Results ---")

for name,response in responses.items():
    print(f"{name} would like to climb {response}.")