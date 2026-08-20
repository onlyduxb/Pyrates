from .items import Item


class Inventory:
    def __init__(self, capacity: int, items: list[Item] = []) -> None:
        self._capacity = capacity
        self._items = items

    def can_pickup(self):
        if len(self._items) < self._capacity:
            return True

    def pickup(self, item: Item):
        if self.can_pickup():
            self._items.append(item)

    def drop(self, item: Item):
        if item in self._items:
            self._items.remove(item)

    def __contains__(self, item: Item):
        return True if item in self._items else False

    def __iter__(self):
        return iter(self._items)
