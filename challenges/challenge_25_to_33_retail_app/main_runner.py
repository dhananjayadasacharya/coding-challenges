import challenge26_grand_total
import challenge27_discounts
import challenge28_membership
import challenge29_tax
import challenge30_promo
import challenge31_payment
import challenge32_min_purchase
import challenge33_loyalty

def main():
    grand_total, total_qty, items = challenge26_grand_total.run()
    grand_total = challenge27_discounts.run(grand_total, total_qty)
    grand_total = challenge28_membership.run(grand_total)
    grand_total = challenge30_promo.run(items)
    grand_total = challenge29_tax.run(grand_total)
    grand_total = challenge31_payment.run(grand_total)

    if challenge32_min_purchase.run(grand_total):
        challenge33_loyalty.run(grand_total)

if __name__ == "__main__":
    main()
