def run():
    code = input("Item Code: ")
    desc = input("Description: ")
    qty = int(input("Quantity: "))
    price = float(input("Price per item: "))

    total = qty * price
    print("Item Total:", total)

    return total, qty, code
