import datetime

class Menu:
    def __init__(self):
        self.items = {
            'Burger': 5.99,
            'Pizza': 8.99,
            'Pasta': 7.49,  
            'Salad': 4.99,
            'Soda': 1.99
        }

    def display(self):
        print("\n--- MENU ---")
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}") #2f mean 2 decimal place
        print("-------------\n")

class Order:
    def __init__(self):
        self.items_ordered = {}

    def add_item(self, item, quantity, menu):
        if item in menu.items:
            if item in self.items_ordered:
                self.items_ordered[item] += quantity
            else:
                self.items_ordered[item] = quantity
            return True
        else:
            return False

    def calculate_subtotal(self, menu):
        subtotal = 0
        for item, qty in self.items_ordered.items():
            price = menu.items[item]
            subtotal += price * qty
        return subtotal

class Bill:
    TAX_RATE = 0.10
    DISCOUNT_RATE = 0.05

    def __init__(self, order, menu):
        self.order = order
        self.menu = menu
        self.subtotal = self.order.calculate_subtotal(menu)
        self.tax = self.subtotal * Bill.TAX_RATE
        self.discount = self.subtotal * Bill.DISCOUNT_RATE if self.subtotal > 50 else 0
        self.total = self.subtotal + self.tax - self.discount

    def print_receipt(self):
        print("\n--- RECEIPT ---")
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for item, qty in self.order.items_ordered.items():
            price = self.menu.items[item] * qty
            print(f"{item} x{qty} = ${price:.2f}")
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Tax (10%): ${self.tax:.2f}")
        print(f"Discount: -${self.discount:.2f}")
        print(f"Total: ${self.total:.2f}")
        print("----------------\n")

# Main program
def main():
    menu = Menu()
    order = Order()

    while True:
        menu.display()
        item = input("Enter item name (or 'done'): ").strip().title()

        if item.lower() == 'done':
            break

        if item in menu.items:
            quantity = input(f"Quantity for {item}: ").strip()
            if quantity.isdigit() and int(quantity) > 0:
                order.add_item(item, int(quantity), menu)
            else:
                print("Invalid quantity. Try again.")
        else:
            print("Item not found. Try again.")

    if order.items_ordered:
        Bill(order, menu).print_receipt()
    else:
        print("No order placed.")

if __name__ == "__main__":
    main()