# -*- coding: utf-8 -*-
from item_updaters import (
    AgedBrieUpdater,
    BackstagePassUpdater,
    ConjuredItemUpdater,
    NormalItemUpdater,
    SulfurasUpdater
)

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = self.get_updater(item)
            updater.update()
        
    def get_updater(self, item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater(item)
        elif item.name.startswith("Conjured"):
            return ConjuredItemUpdater(item)
        else:
            return NormalItemUpdater(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
