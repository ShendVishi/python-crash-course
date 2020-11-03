laptop = 'lenovo'
print("Is laptop == 'lenovo'? I predict True.")
print(laptop == 'lenovo')

print("\nIs laptop == 'HP'? I predict False.")
print(laptop == 'HP')

print("\nIs laptop != 'Asus'? I predict True.")
print(laptop != 'Asus')

print("\nIs laptop != 'Asus' and laptop != 'HP'? I predict True.")
print(laptop != 'Asus' and laptop != 'HP')

print("\nIs laptop != 'Asus' and laptop == 'lenovo'? I predict True.")
print(laptop != 'Asus' and laptop != 'HP')

print("\nIs laptop == 'Lenovo'? I expect False.")
print(laptop == 'Lenovo')

print("\nIs laptop == 'Asus' or laptop == 'lenovo'? I expect True.")
print(laptop == 'Asus' or laptop == 'lenovo')