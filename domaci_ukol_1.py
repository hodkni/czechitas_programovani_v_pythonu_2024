"""Úkol: Implementace Systému Pro Doručování
Část 1: Třídy Položka, Pizza a Nápoj"""

from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float

    def __str__(self):
        return f"{self.name}: {self.price} Kč."

@dataclass
class Pizza(Item):
    ingredients: dict

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_ingredient #Přidává extra ingredienci do pizzy a aktualizuje její cenu.

    def __str__(self):
        return super().__str__() + f" Pizza obsahuje ingredience: {self.ingredients}."
    
@dataclass
class Drink(Item):
    volume: int

    def __str__(self):
        return super().__str__() + f" Nápoj má objem: {self.volume}."



""" Část 2: Třída Order: Reprezentuje objednávku učiněnou zákazníkem."""

@dataclass
class Order:
    customer_name: str
    delivery_adress: str
    items: list
    status: str = "New"

    def mark_delivered(self):
        self.status = "Delivered"
    
    def __str__(self):
        return f"Objednávka zákazníka {self.customer_name}, bydlícího na adrese {self.delivery_adress} zahrnuje položky: {self.items}. Stav objednávky je: {self.status}."


"""Část 3: Třída DeliveryPerson: Reprezentuje doručovatele."""

@dataclass
class DeliveryPerson:
    name: str
    phone_number: str
    available: bool = True
    current_order: Order = None

    def assign_order(self, order):
        if self.available == True:
            self.current_order = order
            self.current_order.status = "On the way"
            self.available = False
        else:
            print("Objednávka nebyla přiřazena. Doručovatel není dostupný.")

    def complete_delivery(self):
        self.current_order.mark_delivered()
        self.available = True

    def __str__(self):
        return f"Doručovatel {self.name}, stav: {self.available}."



margarita = Pizza(name="Margarita", price=200, ingredients={"syr": 150, "rajcata": 50})
margarita.add_extra("olivy", 50, 10)

cola = Drink("Cola", 1.5, 500)

order = Order("Jan Novák", "Pražská 123", [margarita, cola])
print(order)

# Vytvoření řidiče a přiřazení objednávky
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_person.assign_order(order)
print(delivery_person)

# Dodání objednávky
delivery_person.complete_delivery()
print(delivery_person)

# Kontrola stavu objednávky po doručení
print(order)