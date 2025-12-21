# customer class
class customer:
    def __init__(self, customer_id, name, amount_paid, travel_from, travel_to):
        self.customer_id = customer_id
        self.name = name
        self.amount_paid = amount_paid
        self.travel_from = travel_from
        self.travel_to = travel_to


# ship base class
class ship:
    def __init__(self, ship_id, ship_name):
        self.ship_id = ship_id
        self.ship_name = ship_name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def total_amount(self):
        return sum(c.amount_paid for c in self.customers)


# cruise_ship class
class cruise_ship(ship):
    def __init__(self, ship_id, ship_name, cruise_type):
        super().__init__(ship_id, ship_name)
        self.cruise_type = cruise_type

    # list all customer details for this cruise ship
    def get_customer_details(self):
        return self.customers


# cargo_ship class
class cargo_ship(ship):
    def __init__(self, ship_id, ship_name, max_cargo_capacity):
        super().__init__(ship_id, ship_name)
        self.max_cargo_capacity = max_cargo_capacity


# marine_company class
class marine_company:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    # 1. total amount collected
    def total_amount_collected(self):
        return sum(ship.total_amount() for ship in self.ships)

    # 2. total amount per ship
    def total_amount_per_ship(self):
        result = {}
        for ship in self.ships:
            result[ship.ship_name] = ship.total_amount()
        return result
