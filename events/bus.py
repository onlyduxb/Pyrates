# ruff: noqa

from .event import Event
from typing import Any, Callable, cast

type AnyEvent = Event[Any]
type Handler[T: AnyEvent] = Callable[[T], Any]


class EventNotUniqueError(Exception):
    pass


class EventIsNotSubscribedError(Exception):
    pass


class HandlerAlreadySubscribedError(Exception):
    pass


class EventBus:
    def __init__(self) -> None:
        self._subscriptions: dict[type[AnyEvent], list[Handler[AnyEvent]]] = {}

    def subscribe_event(self, event: type[AnyEvent]):
        if event in self._subscriptions:
            raise EventNotUniqueError(
                "The event passed to be subscribed must be unique."
            )
        else:
            self._subscriptions[event] = []

    def subscribe[T: AnyEvent](
        self, event_type: type[T], handler: Handler[T]
    ) -> None:
        if event_type not in self._subscriptions:
            raise EventIsNotSubscribedError("Event is not subscribed.")
        if handler in self._subscriptions[event_type]:
            raise HandlerAlreadySubscribedError(
                "Handler cannot be subscribed to the same event twice."
            )
        else:
            self._subscriptions[event_type].append(cast(Handler[Any], handler))

    def on[T: AnyEvent](self, event_type: type[T]):
        def decorator(handler: Handler[T]):
            self.subscribe(event_type, handler)
            return handler

        return decorator

    def publish(self, event: AnyEvent) -> None:
        for cls in type(event).__mro__:
            for handler in self._subscriptions.get(cls, ()):
                handler(event)