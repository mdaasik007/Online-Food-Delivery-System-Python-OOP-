#======================================================

#               Online Foood Delevery System

#=======================================================


# ------------------------------
# Inheritance
# ------------------------------

class User:
    def __init__(self, user_name, phone):
        self.user_name = user_name
        self.phone = phone

    def __repr__(self):
        return f"Name: {self.user_name}, Phone: {self.phone}"


class Customer(User):
    def __init__(self, user_name, phone, customer_id, address):
        super().__init__(user_name, phone)
        self.customer_id = customer_id
        self.address = address

    def __repr__(self):
        return f"Customer[{self.customer_id}] {self.user_name}, Address: {self.address}"


class DeliveryPartner(User):
    def __init__(self, user_name, phone, partner_id, vehicle_type):
        super().__init__(user_name, phone)
        self.partner_id = partner_id
        self.vehicle_type = vehicle_type
        self.available = True

    def __repr__(self):
        status = "Available" if self.available else "Busy"
        return f"DeliveryPartner[{self.partner_id}] {self.user_name}, Vehicle: {self.vehicle_type}, Status: {status}"


# ------------------------------
# Aggregation
# ------------------------------

class MenuItem:
    def __init__(self, item_id, item_name, item_price):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price

    def __repr__(self):
        return f"{self.item_name} (${self.item_price})"


# ------------------------------
# Composition
# ------------------------------

class OrderItem:
    def __init__(self, menu_item, quantity, price_snapshot):
        self.menu_item = menu_item
        self.quantity = quantity
        self.price_snapshot = price_snapshot

    def get_total(self):
        return self.quantity * self.price_snapshot

    def __repr__(self):
        return f"{self.menu_item.item_name} x {self.quantity} = ${self.get_total()}"


class Order:
    def __init__(self, order_id, customer, restaurant):
        self.order_id = order_id
        self.customer = customer            # Aggregation
        self.restaurant = restaurant        # Aggregation
        self.order_items = []               # Composition
        self.total_amount = 0
        self.delivery_partner = None        # Aggregation
        self.status = "Pending"

    def add_item(self, menu_item, quantity):
        item = OrderItem(menu_item, quantity, menu_item.item_price)
        self.order_items.append(item)
        self.total_amount += item.get_total()

    def assign_delivery_partner(self, partner):
        if partner.available:
            self.delivery_partner = partner
            partner.available = False
        else:
            print("Delivery Partner not available")

    def mark_delivered(self):
        self.status = "Delivered"
        if self.delivery_partner:
            self.delivery_partner.available = True

    def __repr__(self):
        items = "\n   ".join(str(item) for item in self.order_items)
        partner_name = self.delivery_partner.user_name if self.delivery_partner else "Not Assigned"

        return (
            f"\nOrder ID: {self.order_id}\n"
            f"Customer: {self.customer.user_name}\n"
            f"Restaurant: {self.restaurant.restaurant_name}\n"
            f"Status: {self.status}\n"
            f"Items:\n   {items}\n"
            f"Total Amount: ${self.total_amount}\n"
            f"Delivery Partner: {partner_name}\n"
        )


class Restaurant:
    def __init__(self, restaurant_name, location):
        self.restaurant_name = restaurant_name
        self.location = location
        self.menu_items = []      # Aggregation
        self.orders = []          # Composition

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

    def create_order(self, order_id, customer):
        order = Order(order_id, customer, self)
        self.orders.append(order)
        return order

    def __repr__(self):
        return f"{self.restaurant_name} ({self.location})"


# ==========================================
# DEMO
# ==========================================

if __name__ == "__main__":

    # Create Restaurant
    restaurant = Restaurant("Snakers", "Erode")

    # Create Menu Items
    pizza = MenuItem(1, "Pizza", 160)
    biriyani = MenuItem(2, "Biriyani", 200)

    restaurant.add_menu_item(pizza)
    restaurant.add_menu_item(biriyani)

    # Create Customer
    customer1 = Customer("Aasik", "1234567890", 101, "New York")

    # Create Delivery Partner
    partner = DeliveryPartner("Mike", "9876543210", 201, "Bike")

    # Create Order (Composition)
    order1 = restaurant.create_order(1001, customer1)

    # Add items
    order1.add_item(pizza, 2)
    order1.add_item(biriyani, 1)

    # Assign Delivery Partner
    order1.assign_delivery_partner(partner)

    # Print Order
    print(order1)

    # Deliver Order
    order1.mark_delivered()

    print("After Delivery:")
    print(order1)