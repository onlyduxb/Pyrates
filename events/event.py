from ..models import Entity


class Event[T]:
    def __init__(self, source: T) -> None:
        self._source = source

    @property
    def source(self):
        return self._source


class EntityEvent(Event[Entity]):
    pass


class EntityDied(EntityEvent):
    def __init__(self, source: Entity) -> None:
        super().__init__(source)
