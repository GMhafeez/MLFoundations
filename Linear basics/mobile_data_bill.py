def calculate_extra_charges(usage):
    if usage > 8:
        overage = usage - 8
        extra_charges = overage * 3
        return extra_charges
    else:
        return 0.0

def apply_discount(extra):
    if extra > 20:
        discount = extra * 0.10
        return extra - discount
    else:
        return extra

def calculate_tax(amount):

    tax = amount * 0.06
    return tax

def calculate_total_bill(base, extra, tax):

    total = base + extra + tax
    return total

def display_bill(usage, BASE_PLAN, extra, discount, tax, total):

    print("----- MOBILE DATA BILL -----")
    print(f"Data Used: {usage} GB")
    print(f"Base Plan: ${BASE_PLAN:.2f}")
    print(f"Extra Charges: ${extra + discount:.2f}")
    if discount > 0:
        print(f"Discount Applied: ${discount:.2f}")
    print(f"Subtotal: ${BASE_PLAN + extra:.2f}")
    print(f"Tax (6%): ${tax:.2f}")
    print(f"Total Amount Due: ${total:.2f}")
    print("----------------------------")

BASE_PLAN = 25
usage = float(input("Enter data usage (GB): "))

extra_charges_before_discount = calculate_extra_charges(usage)
extra_charges_after_discount = apply_discount(extra_charges_before_discount)
discount_amount = extra_charges_before_discount - extra_charges_after_discount
subtotal = BASE_PLAN + extra_charges_after_discount
tax = calculate_tax(subtotal)
total = calculate_total_bill(BASE_PLAN, extra_charges_after_discount, tax)

# Display the bill
display_bill(usage, BASE_PLAN, extra_charges_after_discount, discount_amount, tax, total)
