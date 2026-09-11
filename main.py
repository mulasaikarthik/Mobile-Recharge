def recharge(plan):
    if plan == 1:
        return 199, "1.5 GB/day"
    elif plan == 2:
        return 299, "2 GB/day"
    elif plan == 3:
        return 399, "2.5 GB/day"
    elif plan == 4:
        return 499, "3 GB/day"
    else:
        return 0, "Invaild Plan"

print("======= MOBILE RECHARGE =======")

mobile = input("Enter Mobile Number: ")

print("\nAvailable Plans:")
print("1. ₹199 - 1.5 GB/day")
print("2. ₹299 - 2 GB/day")
print("3. ₹399 - 2.5 GB/day")
print("4. ₹499 - 3 GB/day")

plan = int(input("\nChoose your plan (1-4): "))

price, data = recharge(plan)

if price == 0:
    print("\nInvaild plan selected")

else:
    print("\n====== RECHARGE DETAILS =======")
    print("Mobile Number:",mobile)
    print("Plan Price:", price)
    print("Data:", data)
    print("Recharge Successful!")
