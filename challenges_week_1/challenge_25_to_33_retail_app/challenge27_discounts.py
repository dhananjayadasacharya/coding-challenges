def run(grand_total, total_qty):
    if grand_total > 10000:
        grand_total *= 0.90

    if total_qty > 20:
        grand_total *= 0.95

    print("After Discounts:", grand_total)
    return grand_total
