amount = int(input("Enter purchased amount = "))

if amount > 5000:
    discount_amt = (20/100) * amount    # Calculates discounted amount
    print("Discounted amount =  ", discount_amt)

elif 1000 <= amount <= 5000:
    discount_amt = 10 / 100 * amount
    print("Discounted amount =  ", discount_amt)

else:
    discount_amt = 0
    print("Discounted amount =  ", discount_amt)
