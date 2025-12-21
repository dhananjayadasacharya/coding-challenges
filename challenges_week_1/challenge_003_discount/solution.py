total_amt = int(input("Enter total amount: "))
discount = int(input("Enter discount percentage: "))

def discount_calculator(tot: int,disc: int):
    return tot-(disc/100)*tot

print(discount_calculator(total_amt,discount))