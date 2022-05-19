
def menu(day):
    if day == "monday":
       food = "veg"
    elif day == "tuesday":
        food = "egg"
    elif day=="wed":
      food = "meat"
    else:
        food="anything"
    print("delicious")
    return food
print(menu("wed"))
