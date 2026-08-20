from typing import Callable, Iterator


class Repository[T]:
    def __init__(self) -> None:
        self._table: set[T] = set()

    def add(self, obj: T):
        self._table.add(obj)

    def remove(self, obj: T):
        self._table.discard(obj)

    def generate[**P](
        self, cls: Callable[P, T], *args: P.args, **kwargs: P.kwargs
    ) -> T:
        obj = cls(*args, **kwargs)
        self._table.add(obj)
        return obj

    def __contains__(self, obj: object) -> bool:
        return obj in self._table

    def __len__(self) -> int:
        return len(self._table)

    def __iter__(self) -> Iterator[T]:
        return iter(self._table)