def run(items):
    total = 0

    for code, qty, item_total in items:
        if code == "PROMO10":
            item_total *= 0.90
        total += item_total

    print("After Promo Discounts:", total)
    return total
