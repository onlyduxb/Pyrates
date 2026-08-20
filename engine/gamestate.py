from ..models import Player

class Gamestate:
    def __init__(self, player: Player) -> None:
        self._player = player