'''
Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until
they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that
topping to their pizza.
'''
toppings_available = ['green olives', 'serrano pepper', 'black olives', 'mushrooms', 'green pepper']
toppings_chosen = []

crust = input("What type of crust do you want? ")

while True:
    topping = input(f"\nWhat topping do you want on your {crust}-crust pizza? Enter 'quit' when you are done. ")

    if topping == 'quit':
        print(f"Your {crust}-pizza with {toppings_chosen} will be ready in no time. ")
        break
    else:
        if topping not in toppings_available:
            print(f"{topping} is not available right now. We apologize! ")
        
        if topping in toppings_chosen:
            print(f"You already have {topping} in your pizza. ")
        else:
            toppings_chosen.append(topping)