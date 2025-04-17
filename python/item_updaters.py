# -*- coding: utf-8 -*-

class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        self.update_quality()
        self.update_sell_in()
        if self.item.sell_in < 0:
            self.handle_expired()

    def update_quality(self):
        pass

    def update_sell_in(self):
        self.item.sell_in -= 1

    def handle_expired(self):
        pass


class NormalItemUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1

    def handle_expired(self):
        if self.item.quality > 0:
            self.item.quality -= 1


class AgedBrieUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

    def handle_expired(self):
        if self.item.quality < 50:
            self.item.quality += 1


class SulfurasUpdater(ItemUpdater):
    def update(self):
        pass


class BackstagePassUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
            if self.item.sell_in < 11 and self.item.quality < 50:
                self.item.quality += 1
            if self.item.sell_in < 6 and self.item.quality < 50:
                self.item.quality += 1

    def handle_expired(self):
        self.item.quality = 0
