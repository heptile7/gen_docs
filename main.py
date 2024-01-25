# main.py
from inventory.product import Product
from inventory.inventory_manager import InventoryManager
from reports.report_generator import ReportGenerator

def main():
    inventory_manager = InventoryManager()

    # Adding some sample products to the inventory
    product1 = Product(1, "Laptop", 800, 10)
    product2 = Product(2, "Mouse", 20, 50)

    inventory_manager.add_product(product1)
    inventory_manager.add_product(product2)

    # Display the initial inventory report
    report_generator = ReportGenerator(inventory_manager)
    print("Initial Inventory Report:")
    report_generator.generate_inventory_report()

    # Update quantity of a product
    inventory_manager.update_quantity(1, 8)

    # Display the updated inventory report
    print("\nUpdated Inventory Report:")
    report_generator.generate_inventory_report()

if __name__ == "__main__":
    main()
