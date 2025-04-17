# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_conjured_item_degrades_twice_as_fast(self):
        items = [Item("Conjured Item", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)

    def test_conjured_item_degrades_twice_as_fast_after_expiry(self):
        items = [Item("Conjured Item", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)
        
if __name__ == '__main__':
    unittest.main()
