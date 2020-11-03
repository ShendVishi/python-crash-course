pizza = {
    'crust': 'thick',
    'toppings': ['black olives', 'mushrooms', 'green olives', 'green pepper']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")