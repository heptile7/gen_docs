# tests/test_inventory_manager.py
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inventory.inventory_manager import InventoryManager
from inventory.product import Product

class TestInventoryManager(unittest.TestCase):
    def test_add_product(self):
        # Your test cases here
        pass

    def test_update_quantity(self):
        # Your test cases here
        pass

# Similar tests can be written for other modules
