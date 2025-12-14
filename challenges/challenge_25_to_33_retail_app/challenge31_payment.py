def run(grand_total):
    mode = input("Payment Mode (cash/card): ")

    if mode.lower() == "card":
        surcharge = grand_total * 0.02
        grand_total += surcharge
        print("Card Surcharge:", surcharge)

    print("Final Payable:", grand_total)
    return grand_total
