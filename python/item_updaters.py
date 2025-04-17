# -*- coding: utf-8 -*-

class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        self.update_quality()
        self.update_sell_in()
        if self.item.sell_in < 0:
            self.handle_expired()
        self.bound_quality()

    def update_quality(self):
        pass

    def update_sell_in(self):
        self.item.sell_in -= 1

    def handle_expired(self):
        pass

    def increase_quality(self, amount=1):
        self.item.quality += amount

    def decrease_quality(self, amount=1):
        self.item.quality -= amount

    def bound_quality(self):
        self.item.quality = max(0, min(50, self.item.quality))


class NormalItemUpdater(ItemUpdater):
    def update_quality(self):
        self.decrease_quality()

    def handle_expired(self):
        self.decrease_quality()


class AgedBrieUpdater(ItemUpdater):
    def update_quality(self):
        self.increase_quality()

    def handle_expired(self):
        self.increase_quality()


class SulfurasUpdater(ItemUpdater):
    def update(self):
        pass


class BackstagePassUpdater(ItemUpdater):
    def update_quality(self):
        self.increase_quality()
        if self.item.sell_in < 11:
            self.increase_quality()
        if self.item.sell_in < 6:
            self.increase_quality()

    def handle_expired(self):
        self.item.quality = 0


class ConjuredItemUpdater(ItemUpdater):
    def update_quality(self):
        self.decrease_quality(2)

    def handle_expired(self):
        self.decrease_quality(2)
