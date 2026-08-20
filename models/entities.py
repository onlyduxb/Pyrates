from common_types import UnitVector, Position
from .items import Weapon
from .item_factory import WeaponType, generate


class Entity:
    def __init__(
        self, health: int, max_health: int, position: Position, weapon: Weapon
    ) -> None:
        self._health = health
        self._max_health = max_health
        self._weapon = weapon
        self._position = position

    @property
    def position(self):
        return self._position

    @property
    def damage(self):
        return self._weapon.damage

    def take_damage(self, damage: float):
        self._health -= damage

    def heal(self, health: int):
        self._health += health

    def move(self, vector: UnitVector) -> Position:
        self._position = (self._position[0] + vector[0], self._position[1] + vector[1])
        return self._position

    def set_position(self, position: Position):
        self._position = position

class Player(Entity):
    def __init__(self, health: int,  position: Position, weapon: Weapon = generate(WeaponType.FIST)) -> None:
        super().__init__(health, 100, position, weapon)