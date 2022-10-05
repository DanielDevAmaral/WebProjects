cart = []
order = ""

while cart != order:
    print("Please, enter the items of the shopping list (type quit to finish): \n")
    order = input("Item: ")
    cart.append(order)
    if order.lower() == "quit":
        cart.remove("quit")
        break

print(f"The shopping list is:")
for itens in cart:
    print(itens)

print()
print(f"The shopping list with indexes is:")
for (i, itens) in enumerate(cart, start=1):
    print(f"{i}. {itens}")

print()

i = int(input("Whitch item do you like to change? "))
new_item = input("What is the new item? ")

cart[i - 1] = new_item

for (i, itens) in enumerate(cart, start=1):
    print(f"{i}. {itens}")




