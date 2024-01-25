# inventory/inventory_manager.py
from inventory.product import Product

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def get_inventory(self):
        return self.inventory

    def update_quantity(self, product_id, new_quantity):
        for product in self.inventory:
            if product.id == product_id:
                product.quantity = new_quantity
                break
