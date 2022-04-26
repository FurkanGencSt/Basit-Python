print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? Small, Medium, or Large(S/M/L) ")
add_pepperoni = input("Do you want pepperoni? Yes or No ")
extra_cheese = input("Do you want extra cheese? Yes or No ")

bill = 0

if size.upper() == "S":
    bill += 15
    if add_pepperoni.upper() == "Y":
        bill += 2
    else:
        pass
    if extra_cheese.upper() == "Y":
        bill += 1
    else:
        pass
    print(f"Your final bill is: ${bill}")

elif size.upper() == "M":
    bill += 20
    if add_pepperoni.upper() == "Y":
        bill += 3
    else:
        pass
    if extra_cheese.upper() == "Y":
        bill += 1
    else:
        pass
    print(f"Your final bill is: ${bill}")


elif size.upper() == "L":
    bill += 25
    if add_pepperoni.upper() == "Y":
        bill += 3
    else:
        pass
    if extra_cheese.upper() == "Y":
        bill += 1
    else:
        pass
    print(f"Your final bill is: ${bill}")

