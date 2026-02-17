total=float(input("Enter the total cost: "))
paid=float(input("Enter the amount you paid: "))

def amount_left(total,paid):
     due=total-paid
     return due


print("\n The due amount is:",amount_left(total, paid))
