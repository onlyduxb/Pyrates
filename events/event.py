# ruff: noqa

class Event[T]:
    def __init__(self, source: T) -> None:
        self._source = source

    @property
    def source(self):
        return self._source