from enum import auto, Enum


class Rarity(Enum):
    SEA_WRECKED = auto()
    BATTLE_TESTED = auto()
    FINE = auto()
    WORTHY = auto()
    FIRST_RATE = auto()


RARITY_MULTIPLIERS = {
    Rarity.SEA_WRECKED: 0.75,
    Rarity.BATTLE_TESTED: 0.9,
    Rarity.FINE: 1.0,
    Rarity.WORTHY: 1.25,
    Rarity.FIRST_RATE: 1.50,
}


class Item:
    def __init__(self, name: str) -> None:
        self._name = name


class Weapon(Item):
    def __init__(self, name: str, base_damage: int, reach: float, rarity: Rarity) -> None:
        super().__init__(name)
        self._base_damage = base_damage
        self._reach = reach
        self._rarity = rarity

    @property
    def damage(self):
        return int(self._base_damage * RARITY_MULTIPLIERS[self._rarity])

    @property
    def reach(self):
        return self._reach

    @property
    def rarity(self):
        return self._rarity


class Consumable(Item):
    def __init__(self, name: str) -> None:
        super().__init__(name)
