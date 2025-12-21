class HealWellHospital:
    GST_RATE = 0.18

    def __init__(self, services, costs):
        self.services = services
        self.costs = costs
        self.patient = {}
        self.selected_services = []
        self.selected_costs = []
        self.subtotal = 0

    # Level 1: Patient details
    def get_patient_details(self):
        self.patient["name"] = input("Enter Name: ")
        self.patient["age"] = int(input("Enter Age: "))
        self.patient["gender"] = input("Enter Gender: ")
        self.patient["contact"] = input("Enter Contact: ")

    # Level 2: Display services & selection
    def display_services(self):
        print("\nAvailable Services:")
        for i, service in enumerate(self.services, 1):
            print(f"{i}. {service}")

        choices = input("Enter service numbers (comma separated): ")
        indices = [int(x) - 1 for x in choices.split(",")]

        for i in indices:
            self.selected_services.append(self.services[i])
            self.selected_costs.append(self.costs[i])

    # Level 4: Calculate subtotal
    def calculate_subtotal(self):
        self.subtotal = sum(self.selected_costs)
        return self.subtotal

    # Level 8: Discounts
    def apply_discounts(self):
        discount = 0

        if self.patient["age"] >= 60:
            discount += 0.10 * self.subtotal

        if self.subtotal > 5000:
            discount += 0.05 * (self.subtotal - discount)

        return discount

    # Level 5: GST
    def calculate_gst(self, amount):
        return amount * self.GST_RATE

    # Level 6: Invoice
    def generate_invoice(self):
        discount = self.apply_discounts()
        taxable_amount = self.subtotal - discount
        gst = self.calculate_gst(taxable_amount)
        grand_total = taxable_amount + gst

        print("\n" + "-" * 45)
        print("HealWell Care Hospital")
        print("Patient Invoice")
        print("-" * 45)

        print("Patient Information:")
        for key, value in self.patient.items():
            print(f"{key.capitalize()}: {value}")

        print("\nServices Availed:")
        for i in range(len(self.selected_services)):
            print(f"{i+1}. {self.selected_services[i]}: ₹{self.selected_costs[i]}")

        print(f"\nSubtotal: ₹{self.subtotal}")
        print(f"Discount: ₹{discount}")
        print(f"GST (18%): ₹{gst:.2f}")
        print(f"Grand Total: ₹{grand_total:.2f}")

        print("\nThank you for choosing HealWell Care Hospital!")
        print("-" * 45)


# ------------------ MAIN ------------------

services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]

hospital = HealWellHospital(services, costs)

hospital.get_patient_details()
hospital.display_services()
hospital.calculate_subtotal()
hospital.generate_invoice()
