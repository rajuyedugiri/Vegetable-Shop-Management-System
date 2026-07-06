# MINI PROJECT ON VEGETABLE SHOP MANAGEMENT SYSTEM

# Vegetable Details
veg_name = ["tomato", "onion", "brinjal", "potato", "cabbage", "cucumber", "beetroot", "carrot", "spinach", "broccoli", "cauliflower", "green beans", "green chilli", "bottle gourd", "bitter gourd", "coriander", "ladyfinger", "capsicum", "drumstick", "ridge gourd"]

stock = [20, 15, 10, 20, 30, 25, 25, 20, 30, 15, 20, 30, 40, 10, 20, 25, 30, 25, 25, 20]
price = [30, 25, 40, 20, 25, 30, 25, 30, 30, 60, 40, 30, 30, 25, 20, 25, 30, 40, 30, 25]
cost = [20, 18, 28, 18, 22, 25, 18, 20, 18, 30, 18, 18, 15, 18, 15, 15, 18, 20, 20, 18]

# Report Variables (parallel lists, same length as veg_name)
sold = [0] * len(veg_name)
profit_per_veg = [0] * len(veg_name)
total_sale = 0
total_profit = 0
total_bills = 0

# Add Vegetable
def add_vegetable():
    name = input("Enter Vegetable Name: ")

    if name in veg_name:
        print("Vegetable Already Exists")
        return

    qty = int(input("Enter Stock in kgs: "))
    cp = int(input("Enter Cost Price: "))
    sp = int(input("Enter Selling Price: "))

    veg_name.append(name)
    stock.append(qty)
    cost.append(cp)
    price.append(sp)
    sold.append(0)
    profit_per_veg.append(0)

    print("Vegetable Added Successfully")

# Update Vegetable
def update_vegetable():
    name = input("Enter Vegetable Name: ")

    found = -1
    for i in range(len(veg_name)):
        if veg_name[i] == name:
            found = i
            break

    if found == -1:
        print("Vegetable Not Found")
        return

    added_stock = int(input("Enter Stock to Add (kg): "))
    stock[found] = stock[found] + added_stock

    cost[found] = int(input("Enter New Cost Price: "))
    price[found] = int(input("Enter New Selling Price: "))

    print(f"Updated Successfully. New Stock: {stock[found]} kg")

# Delete Vegetable
def delete_vegetable():
    name = input("Enter Vegetable Name: ")

    found = -1
    for i in range(len(veg_name)):
        if veg_name[i] == name:
            found = i
            break

    if found == -1:
        print("Vegetable Not Found")
        return

    del veg_name[found]
    del stock[found]
    del price[found]
    del cost[found]
    del sold[found]
    del profit_per_veg[found]

    print("Deleted Successfully")

# Shopkeeper Reports
def veg_report():
    print("\n==========================================")
    print(f"{'VEG REPORT':^42}")
    print("==========================================")
    print(f"{'Vegetable':<18}{'Stock (kg)'}")
    print("-" * 40)
    for i in range(len(veg_name)):
        print(f"{veg_name[i]:<18}{stock[i]}")

def revenue_report():
    print("\n==========================================")
    print(f"{'REVENUE REPORT':^42}")
    print("==========================================")
    print(f"Total Revenue : Rs. {total_sale}")
    print(f"Total Profit  : Rs. {total_profit}")
    print(f"Total Bills   : {total_bills}")

def itemized_profit_report():
    print("\n=====================================================")
    print(f"{'ITEMIZED PROFIT REPORT':^54}")
    print("=====================================================")
    print(f"{'Vegetable':<18}{'Sold Qty':<12}{'CP':<8}{'SP':<8}{'Profit'}")
    print("-" * 54)
    for i in range(len(veg_name)):
        qty_text = f"{sold[i]:>3} kg"
        print(f"{veg_name[i]:<18}{qty_text:<12}{cost[i]:<8}{price[i]:<8}{profit_per_veg[i]}")

def reports():
    while True:
        print("\n----- REPORT MENU -----")
        print("1. Veg Report")
        print("2. Revenue Report")
        print("3. Itemized Profit Report")
        print("4. Back")

        ch = input("Enter Choice: ")

        if ch == "1":
            veg_report()
        elif ch == "2":
            revenue_report()
        elif ch == "3":
            itemized_profit_report()
        elif ch == "4":
            break
        else:
            print("Invalid Choice")

# Shopkeeper Menu 
def shopkeeper():
    while True:
        print("\n----- SHOPKEEPER -----")
        print("1. Add Vegetable")
        print("2. Update Vegetable")
        print("3. Delete Vegetable")
        print("4. Reports")
        print("5. Back")

        ch = input("Enter Choice: ")

        if ch == "1":
            add_vegetable()
        elif ch == "2":
            update_vegetable()
        elif ch == "3":
            delete_vegetable()
        elif ch == "4":
            reports()
        elif ch == "5":
            break
        else:
            print("Invalid Choice")

# Customer
def customer():
    global total_sale
    global total_profit
    global total_bills

    bill = 0
    item_names = []
    item_qtys = []
    item_amounts = []

    while True:
        print(f"\n{'S.No':<6}{'Vegetable':<18}{'Stock':<8}{'Price'}")
        print("-" * 42)

        for i in range(len(veg_name)):
            print(f"{i + 1:<6}{veg_name[i]:<18}{stock[i]:<8}{price[i]}")

        name = input("\nEnter Vegetable Name (or Done): ")

        if name == "Done" or name == "done":
            break

        found = -1
        for i in range(len(veg_name)):
            if veg_name[i] == name:
                found = i
                break

        if found == -1:
            print("Vegetable Not Found")
            continue

        qty = int(input("Enter Quantity (kg): "))

        if qty > stock[found]:
            print("Sorry, Out of Stock")
            continue

        amount = qty * price[found]
        profit = qty * (price[found] - cost[found])

        stock[found] = stock[found] - qty
        sold[found] = sold[found] + qty
        profit_per_veg[found] = profit_per_veg[found] + profit

        total_sale = total_sale + amount
        total_profit = total_profit + profit

        bill = bill + amount

        item_names.append(veg_name[found])
        item_qtys.append(qty)
        item_amounts.append(amount)

        print("Item Added to Bill")

    if bill > 0:
        total_bills = total_bills + 1

        print("\n==========================================")
        print(f"{'CUSTOMER BILL':^42}")
        print("==========================================")
        print(f"{'Vegetable':<18}{'Qty (kg)':<12}{'Amount'}")
        print("------------------------------------------")

        for i in range(len(item_names)):
            print(f"{item_names[i]:<18}{item_qtys[i]:<12}{item_amounts[i]}")

        print("------------------------------------------")
        total_text = f"Total: Rs. {bill}"
        print(f"{total_text:>42}")
        print("==========================================")
    else:
        print("\nNo items purchased.")

# Main Menu
while True:

    print("\n==============================")
    print("VEGETABLE SHOP MANAGEMENT")
    print("==============================")
    print("1. Shopkeeper")
    print("2. Customer")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        shopkeeper()
    elif choice == "2":
        customer()
    elif choice == "3":
        print("Closing the shop....")
        break
    else:
        print("Invalid Choice")