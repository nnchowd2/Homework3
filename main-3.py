# Name: Nafisa Chowdhury
# PSID: 1591144
# CHANGE

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price,
                                                 self.item_quantity * self.item_price))


if __name__ == "__main__":
    item1 = ItemToPurchase()

    item1.item_name = input("Item 1\nEnter the item name:\n")
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    item2 = ItemToPurchase()

    item2.item_name = input("\nItem 2\nEnter the item name:\n")
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    Total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    print()
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print("Total: ${:0.0f}".format(Total))
