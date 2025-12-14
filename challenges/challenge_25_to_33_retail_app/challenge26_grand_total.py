def run():
    grand_total = 0
    total_qty = 0
    items = []

    n = int(input("Enter number of items: "))

    for _ in range(n):
        code = input("Item Code: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        total = qty * price

        items.append((code, qty, total))
        grand_total += total
        total_qty += qty

    print("Grand Total:", grand_total)
    return grand_total, total_qty, items
