class ShoppingCart:
    def __init__(self, payment_gateway=None):
        self.items = {}
        self.discount = 0  # Porcentaje de descuento
        self.payment_gateway = payment_gateway  # Inyección de dependencia
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
