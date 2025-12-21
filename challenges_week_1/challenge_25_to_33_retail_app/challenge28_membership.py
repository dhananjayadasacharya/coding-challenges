def run(grand_total):
    member = input("Are you a member (y/n)? ")

    if member.lower() == 'y':
        grand_total *= 0.98

    print("After Membership Discount:", grand_total)
    return grand_total
