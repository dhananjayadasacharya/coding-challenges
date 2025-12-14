def run(grand_total):
    if grand_total < 5000:
        tax = grand_total * 0.05
    elif grand_total <= 20000:
        tax = grand_total * 0.10
    else:
        tax = grand_total * 0.15

    grand_total += tax
    print("Tax:", tax)
    print("After Tax:", grand_total)
    return grand_total
