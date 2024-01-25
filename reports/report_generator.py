# reports/report_generator.py
from inventory.inventory_manager import InventoryManager

class ReportGenerator:
    def __init__(self, inventory_manager):
        self.inventory_manager = inventory_manager

    def generate_inventory_report(self):
        for product in self.inventory_manager.get_inventory():
            print(product)
