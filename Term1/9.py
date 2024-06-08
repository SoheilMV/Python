products = ["Ice Cream", "Chips", "Yoghurt", "Milk", "Eggs", "Flour"]
prices = [15, 20, 70, 20, 135, 60]

for i in range(len(products)):
    print(f"{products[i]} => {prices[i]}")
print()

price = 0
while True:
    product = input("Please select your desired product: ").title()
    if product in products:
        index = products.index(product)
        price += prices[index]
    elif product.lower() == "end":
        break
    else:
        print("Product not found!")

print(f"Price => {price}")