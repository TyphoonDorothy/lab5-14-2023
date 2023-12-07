"""
Used for keeping track of expiration dates
"""
from datetime import datetime


class Medicine:
    """
    Specific medicine
    """
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_prescription_needed = args[0]
        self.expiration_date = args[1]

    def is_expired(self):
        """
        Checks if medicine is expired
        """
        return datetime.now() > self.expiration_date

    def is_prescribed(self):
        """
        Tells if medicine needs prescriptions
        """
        return self.is_prescription_needed


class Pharmacy:
    """
    A list of all medicines
    """
    def __init__(self):
        self.inventory = []

    def add_medicine(self, medicine):
        """
        Adds medicine to inventory
        """
        self.inventory.append(medicine)

    def remove_expired_medicines(self):
        """
        Removes expired medicine from stock
        """
        self.inventory = [medicine for medicine in self.inventory if not medicine.is_expired()]

    def apply_discount(self):
        """
        Makes all medicine cheaper by 10%
        """
        for medicine in self.inventory:
            medicine.price -= 0.1 * medicine.price

    def sort_by_price(self, medicine):
        """
        Returns all medicine sorted by price
        """
        return medicine.price

    def get_cheapest_medicine(self, count=1):
        """
        Returns the cheapest medicine
        """
        sorted_meds = sorted(self.inventory, key=self.sort_by_price)
        return sorted_meds[:count]

    def remove_medicine(self, medicine_name):
        """
        Removes specific medicine
        """
        self.inventory = [medicine for medicine in self.inventory
                          if not medicine.name == medicine_name]

    def __str__(self):
        inventory_str = "\n".join([f'{medicine.name} - Price: {medicine.price}, '
                                   f'Quantity: {medicine.quantity}'
                                   for medicine in self.inventory])
        return f"Pharmacy Inventory: \n{inventory_str}"


paracetamol = Medicine("Paracetamol", 20.0, 100, False, datetime(2023, 12, 31))
aspirin = Medicine("Aspirin", 15.0, 50, True, datetime(2027, 6, 30))
ibuprofen = Medicine("Ibuprofen", 30.0, 80, False, datetime(2023, 8, 15))

pharmacy = Pharmacy()
pharmacy.add_medicine(paracetamol)
pharmacy.add_medicine(aspirin)
pharmacy.add_medicine(ibuprofen)
print(pharmacy)

pharmacy.remove_expired_medicines()
print("\n", pharmacy)

pharmacy.apply_discount()
print("\n", pharmacy)

cheapest_meds = pharmacy.get_cheapest_medicine()
for med in cheapest_meds:
    print(f"The cheapest medicine: {med.name}, Price: {med.price}")

pharmacy.remove_medicine("Aspirin")
print("\n", pharmacy)
