from .items import Rarity, Item, Weapon, Consumable
from dataclasses import dataclass
from typing import overload
from enum import Enum


@dataclass(frozen=True)
class ItemTemplate:
    name: str

@dataclass(frozen=True)
class WeaponTemplate(ItemTemplate):
    base_damage: int
    reach: float
    rarity: Rarity = Rarity.FINE



@dataclass(frozen=True)
class ConsumableTemplate(ItemTemplate):
    pass


class ItemType(Enum):
    def generate(self) -> Item:
        template: ItemTemplate = self.value
        return Item(template.name)


class WeaponType(ItemType, Enum):
    FIST = WeaponTemplate("Fist", 5, 1)
    CUTLASS = WeaponTemplate("Cutlass", 12, 1.0)
    FLINTLOCK = WeaponTemplate("Flintlock", 40, 2.0)
    BLUNDERBUSS = WeaponTemplate("Blunderbuss", 25, 5)

    def generate(self) -> Weapon:
        template: WeaponTemplate = self.value
        return Weapon(
            name=template.name,
            base_damage=template.base_damage,
            reach=template.reach,
            rarity=template.rarity,
        )


class ConsumableType(ItemType, Enum):
    BANDAGE = ConsumableTemplate("Bandage")
    LINT = ConsumableTemplate("Lint")

    def generate(self) -> Consumable:
        template: ConsumableTemplate = self.value
        return Consumable(name=template.name)


@overload
def generate(item_type: WeaponType) -> Weapon: ...


@overload
def generate(item_type: ConsumableType) -> Consumable: ...


def generate(item_type: ItemType):
    return item_type.generate()