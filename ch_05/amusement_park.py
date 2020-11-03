age = 12
# if(age < 4):
#     print("Admission for you is free.")
# elif(age < 18):
#     print("Admission for you is $5")
# else:
#     print("Admission for you is $10")

if(age < 4):
    price = 0
elif(age < 18):
    price = 5
elif(age < 65):
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")