def welcome():
    print("Heavenly Pizza")
    print("*" * 60)
    print("Welcome to Heavenly Pizza's online ordering system")
    print()
    print("This system enables us to be able to offer contactless pick-up\
and delivery service for our customers during this coronavirus pandemic")
    print()
    print("- Please note due to the circumstances there is a restriction of\
3 pizzas per order")
    print("- We also do strongly recommend the avoid payment by cash where\
possible, and prefer contactless payments such as paywave")
    print("- We have 1 Vegan pizza option, labelled (Vegan)")
    print("- None of our pizza's are gluten free")
    print()
    print("*" * 60)

    # Printing the Regular menu
    print("Regular Menu: ${}".format(REGULARPRICE))
    v = 0
    for i in regular_menu:
        print(v, i, regular_menu[i])
        v += 1

    print()

    # Printing the Gourmet menu
    print("Gourmet Menu: ${}".format(GOURMETPRICE))
    v = 0
    for i in gourmet_menu:
        print(v, i, gourmet_menu[i])
        v += 1


def ordering():
    # variable to keep track of how many pizzas have been ordered so far
    pizza_amount = 0

    # Creating the full order list (Paralell lists)
    full_order = []
    total_amount = []

    # Loops choosing the options until 3 pizzas are ordered or they quit
    while pizza_amount != MAXORDER:
        # List to append the users order to
        pizza_order = []
        order_amount = []

        # input to store which menu the user is ordering from for the pizza to be used later
        print()
        print("*" * 60)

        menu = check_string_valid("Which menu would you like to order from (Regular'R', \
Gourmet'G', or Quit'Q')")
        print()

        # appending choice to the order list
        if menu == "r":
            menu = "Regular"
            pizza_order.append(menu)
            order_amount.append(REGULARPRICE)

            while True:
                pizza_choice = int(input("What pizza would you like to order?"))
                if pizza_choice < 0 or pizza_choice > 5:
                    print("This is invalid, please re-enter")
                    print()
                else:
                    pizza_choice = list(regular_menu)[pizza_choice]
                    pizza_order.append(pizza_choice)
                    print()
                    break

        elif menu == "g":
            menu = "Gourmet"
            pizza_order.append(menu)
            order_amount.append(GOURMETPRICE)

            while True:
                pizza_choice = int(input("What pizza would you like to order?"))
                if pizza_choice < 0 or pizza_choice > 5:
                    print("This is invalid, please re-enter")
                    print()
                else:
                    break
                    pizza_choice = list(gourmet_menu)[pizza_choice]
                    pizza_order.append(pizza_choice)
                    print()
                    break

        elif menu == "q":
            break

        while True:
            try:
                # input crust choice
                crust_choice = input("Would you like to add stuffed crust for ${} (Yes 'y'\
or No 'n')".format(STUFFEDCRUST)).lower().strip()
                # If the user chooses "n" it will change it to "No stuffed crust to append to the list for easier printing later
                if crust_choice == "n":
                    crust_choice = "No stuffed crust"
                    pizza_order.append(crust_choice)
                    order_amount.append(0)
                    break
                # If the user chooses "y" it will change it to "Stuffed crust" to append to the list for easier printing later
                elif crust_choice == "y":
                    crust_choice = "Stuffed crust"
                    pizza_order.append(crust_choice)
                    order_amount.append(STUFFEDCRUST)
                    break
                elif crust_choice != "n" and crust_choice != "y":
                    print("This is not one of the options, please re-enter")
                    print()
            except:
                break

        # Asks how many of that pizza choice they want
        while True:
            try:
                print()
                quantity = int(input("Quantity of this pizza:"))
                # Increases the pizza amount by the quantity to keep track of how many pizzas ordered so far
                pizza_amount += quantity
                print()
                if pizza_amount > 3:
                    print("There is a limit of 3 pizza's, please re-enter")
                    pizza_amount -= quantity
                else:
                    break
            except:
                print("This is an invalid entry, please enter a number")

        pizza_order.append(quantity)
        order_amount.append(quantity)

        full_order.append(pizza_order)
        total_amount.append(order_amount)
    # total_cost = calculations(total_amount)
    display_order(full_order, total_amount)

    while True:
        confirm = input("To confirm your order is correct and you would like to \
continue enter 'c' if you would like to restart enter 'r'")
        if confirm == "r":
            ordering()
        elif confirm == "c":
            customer_information(full_order, total_amount)
        else:
            print("This is an invalid entry, please choose one of the options")
            print()


def display_order(full_order, total_amount):
    pizza_prices_total = []

    print()
    # printing all the pizzas ordered which were stored in paralell lists
    for i in range(len(full_order)):
        price_pizza = total_amount[i][0] * full_order[i][3] + total_amount[i][1] * full_order[i][3]
        pizza_prices_total.append(price_pizza)
        print("{}x {} {} pizza with {}: ${} ".format(full_order[i][3], full_order[i][0], full_order[i][1],
                                                     full_order[i][2], price_pizza))
        print()


def customer_information(full_order, total_amount):
    print()
    print("*" * 60)
    name = input("Name:")
    phone = input("Phone Number:")

    while True:
        collection_choice = input("Would you like to get your order delivered 'd' \
or pick-up 'p'")
        if collection_choice == "d":
            address = input("Address:")
            print()
            print("Please Note: There is a delivery fee of $8{}".format(DELIVERYFEE))
            print("*" * 60)
            print_all_order(name, phone, address, collection_choice, full_order, total_amount, pizza_price_total)
            print("*" * 60)

        elif collection_choice == "p":
            print_all_order(name, phone, address, collection_choice, full_order, total_amount, pizza_prices_total)
            print("*" * 60)
        else:
            print("This isn't one of the options, please re-enter")
            print()


def print_all_order(name, phone, address, collection_choice, full_order, total_amount, pizza_prices_total):
    print()
    print("Order details:")
    print()
    print("Name: {}".format(name))
    print("Phone number: {}".format(phone))
    if collection_choice == "d":
        print("Address: {}".format(address))
        print()
        print("Delivery Fee: ${}".format(DELIVERYFEE))
    print()
    display_order(full_order, total_amount)

    for i in range(len(total_amount)):
        total_cost = sum(pizza_prices_total)
    print("*" * 60)


def check_string_valid(prompt):
    while True:
        try:
            i = input(prompt).lower().strip()
            if i != "r" and i != "g" and i != "q":
                print("This is not an option, please re-enter")
                print()
            else:
                return i
                break
        except:
            break


# Main Routine
# Regular pizzas and ingredients stored in a dictionary
regular_menu = {"Margherita: ": "(Fresh tomato, mozzarella, fresh basil,\
parmesan)",
                "Kiwi": ": (Bacon, egg, mozzarella)",
                "Garlic": ": (Mozzarella, garlic)",
                "Cheese": ": (Mozzarella, oregano)",
                "Hawaiian": ": (Ham, pineapple, mozzarella)",
                "Mediterranean (Vegan)": ": (Lebanese herbs, olive oil, fresh tomatoes, \
olives, onion)"
                }

# Gourmet pizzas and ingredients stored in a dictionary
gourmet_menu = {"Meat": ": (Bacon, pancetta, ham, onion, pepperoni, mozzarella)",
                "Chicken Cranberry": ": (Smoked chicken, cranberry, camembert mozzarella)",
                "Satay Chicken": ": (Smoked chicken, onions, capsicum, pine nuts, satay sauce, \
mozzarella, Chilli flakes and dried basil)",
                "Big BBQ Bacon": ": (Smoky Bacon served on our classic marinara tomato sauce, \
heaped with mozzarella, topped off with a sweet and tangy BBQ drizzle)",
                "Veggie": ": (sweet red onion, mushroom, red capsicum & melting mozzarella \
with drizzles of our tangy roast capsicum drizzle, finished with a dash of \
oregano.)",
                "Meatlovers": ": (Spicy pepperoni, Italian sausage, succulent ham, \
seasoned ground beef and crispy bacon all piled onto classic marinara sauce\
and finished with cheesy mozzarella and a drizzle of BBQ sauce.)"
                }

REGULARPRICE = 8
GOURMETPRICE = 15
STUFFEDCRUST = 3
DELIVERYFEE = 8
MAXORDER = 3

welcome()
ordering()
