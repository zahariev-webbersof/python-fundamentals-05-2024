class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            return True
        return False

    def get_items(self):
        return self.items


import unittest


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_add_new_item(self):
        result = self.inventory.add_item('apple')
        self.assertTrue(result)
        self.assertIn('apple', self.inventory.get_items())