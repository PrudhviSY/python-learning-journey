customer_name = input("what is your name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"Total amount for {customer_name}: ${total:.2f}")