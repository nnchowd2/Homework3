# Name: Nafisa Chowdhury
# PSID: 1591144

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price))

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self):
        print("ADD ITEM TO CART")
        name = input("Enter the item name:\n")
        description = input("Enter the item description:\n")
        price = int(input("Enter the item price:\n"))
        quantity = int(input("Enter the item quantity:\n"))
        self.cart_items.append(ItemToPurchase(name, price, quantity, description))

    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        remove_item = input("Enter name of item to remove:\n")
        for item in self.cart_items:
            if item.item_name == remove_item:
                del self.cart_items[item]
                break
        if item.item_name != remove_item:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self):
        print()
        print("CHANGE ITEM QUANTITY")
        name = input("Enter the name of item:\n")
        for item in self.cart_items:
            if item.item_name == name:
                quantity = int(input("Enter the new quantity:\n"))
                item.item_quantity = quantity
                break
            else:
                print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        sum = 0
        for item in self.cart_items:
            sum += item.item_quantity
        return sum

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += (item.item_price * item.item_quantity)
        return total

    def print_total(self):
        s = ShoppingCart()
        total_cost = 0
        print("OUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        if s.get_cost_of_cart() == 0:
            print("Number of Items: 0")
            print()
            print("SHOPPING CART IS EMPTY")
            print()
            print("Total: $0")
        else:
            print("Number of Items: {}".format(s.get_num_items_in_cart()))
            print()
            if self.cart_items == 0:
                print("SHOPPING CART IS EMPTY")
            else:
                for item in self.cart_items:
                    print("{} {} @ ${} = ${}".format(item.item_name, item.item_quantity, item.item_price, item.item_price * item.item_quantity))
                    total_cost += item.item_price * item.item_quantity
                print()
                print("Total: ${}".format(total_cost))

    def print_descriptions(self):
        if self.cart_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("OUTPUT ITEMS' DESCRIPTIONS")
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print()
            print("Item Descriptions")
            for item in self.cart_items:
                item.print_item_description()


def print_menu(ShoppingCart):
    c = Cart
    choice = ""
    while choice != "q":
        print()
        print("MENU")
        print("a - Add item to cart\n"
              "r - Remove item from cart\n"
              "c - Change item quantity\n"
              "i - Output items' descriptions\n"
              "o - Output shopping cart\n"
              "q - Quit")
        print()
        choice = input("Choose an option:\n")
        while choice != "a" and choice != "r" and choice != "c" and choice != "i" and choice != "o" and choice != "q":
            choice = input("Choose an option:\n")
        if choice == "a":
            c.add_item()
        if choice == "r":
            c.remove_item()
        if choice == "c":
            c.modify_item()
        if choice == "i":
            c.print_descriptions()
        if choice == "o":
            c.print_total()


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print()
    print("Customer name:", customer_name)
    print("Today's date:", current_date)
    Cart = ShoppingCart(customer_name, current_date)
    print_menu(Cart)

