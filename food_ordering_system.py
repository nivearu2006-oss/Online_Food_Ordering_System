import json
import os
MENU_FILE="menu.json"
ORDERS_FILE="orders.json"
def load_menu():
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE,"r")as f:
            return json.load(f)
    else:
        menu={
            "1":{"name":"Veg Biryani","price":120},
            "2":{"name":"Chicken Biryani","price":150},
            "3":{"name":"Gobi Manchurian","price":90},
            "4":{"name":"Gulab Jamun","price":40},
            "5":{"name":"Coca-Cola","price":30}
        } 
        save_menu(menu)
        return menu
def save_menu(menu):
    with open(MENU_FILE,"w")as f: 
        json.dump(menu,f,indent=4)
def display_menu(menu):
    print("\n=====FOOD MENU=====")
    for key in menu:
        print(key+"."+menu[key]["name"]+"-Rs."+str(menu[key]["price"]))
    print("======================")
def save_order(order):
    orders=[]
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE,"r")as f:
            orders=json.load(f)
    orders.append(order)
    with open(ORDERS_FILE,"w")as f:
        json.dump(orders,f,indent=4)
def place_order(menu):
    cart={}
    name=input("Enter your name:")
    while True:
        display_menu(menu)
        choice=input("Enter item number to add(or'done' to finish):")
        if choice=="done":
            break
        if choice in menu:
            qty=int(input("Enter quantity:"))
            if choice in cart:
                cart[choice]+=qty
            else:
                cart[choice]=qty
            print(menu[choice]["name"]+"added to cart.")
        else:
            print("Invalid item number.")
    total=0
    print("\n=====YOUR ORDER=====")
    for item_id in cart:
        item_name=menu[item_id]["name"]
        item_price=menu[item_id]["price"]
        qty=cart[item_id]
        subtotal=item_price*qty
        total=total+subtotal
        print(item_name+"x"+str(qty)+"=Rs."+str(subtotal))
    print("TOTAL=Rs."+str(total))
    print("=======================")
    if total >0:
        address=input("Enter delivery address:")
        order={
            "customer":name,
            "address":address,
            "items":cart,
            "total":total,
            "status":"Confirmed"
        }
        save_order(order)
        print("\nOrder placed successfully! Thank you"+name+"!")
    else:
        print("cart is empty.Order cancelled.")
def view_all_orders():
    if not os.path.exists(ORDERS_FILE):
        print("No order yet.")
        return
    with open(ORDERS_FILE,"r")as f:
        orders=json.load(f)
    if len(orders)==0:
        print("No order yet.")
        return
    total_sales=0
    print("\n=====ALL ORDERS=====")
    for i in range(len(orders)):
        o=orders[i]
        print(str(i+1)+"."+o["customer"]+"Rs."+str(o["total"])+"-"+o["status"])
        total_sales=total_sales+o["total"]
    print("TOTAL SALES:Rs."+str(total_sales))
    print("=======================")
def add_new_item(menu):
    new_id=str(len(menu)+1)
    name=input("Enter new item name:")
    price=float(input("Enter price:"))
    menu[new_id]={"name":name,"price":price}
    save_menu(menu)
    print(name+"added to menu!")
def admin_panel(menu):
    while True:
        print("\n---ADMIN PANEL---")
        print("1.View Orders")
        print("2.Add New Item")
        print("3.View Menu")
        print("4.Back to Main Menu")
        choice=input("Enter choice:")
        if choice=="1":
            view_all_orders() 
        elif choice=="2":
            add_new_item(menu)
        elif choice=="3":
            display_menu(menu)
        elif choice=="4":
            break 
        else:
            print("Invalid ckoice.")
def main():
    menu=load_menu()
    print("=====================================")
    print("WELCOME TO NIVETHA'S FOOD ORDERING APP")
    print("=====================================")
    while True:
        print("\n1.Customer-Place Order")
        print("2.Admin Login")
        print("3.Exit")
        choice=input("Enter choice:")
        if choice=="1":
            place_order(menu)
        elif choice=="2":
            pw=input("Enter admin password:")
            if pw=="admin123":
                admin_panel(menu)
            else:
                print("Wrong password!")
        elif choice=="3":
            print("Thank you!Goodbye!")
            break
        else:
            print("Invalid choice.")
main()              
                                                         



                  