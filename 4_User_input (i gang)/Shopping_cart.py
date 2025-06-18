item = input("what item do you want to buy?: ")
price = float(input(f"What is the {item}'s price: "))
quantity = int(input(f"How many {item}s item would you like to buy?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}s")
# You can use the round function, round down a float to a selected amount og decimals efter komma
# Here we have chosen 2 decimals after the comma
print(f"Your total is going to be: {round(total, 2)} DKK")