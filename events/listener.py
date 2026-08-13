# ruff: noqa

from .bus import EventBus, AnyEvent
from typing import Callable, Any

def on_event[T: AnyEvent](event_type: type[T]):
    def decorator(func: Callable[..., Any]):
        if not hasattr(func, "_subscribed_events"):
            func._subscribed_events = [] # type: ignore
        func._subscribed_events.append(event_type) # type: ignore
        return func
    return decorator

class EventListener:
    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        self._register_handlers()

    def _register_handlers(self) -> None:
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if hasattr(attr, "_subscribed_events"):
                for event_type in attr._subscribed_events:
                    self._bus.subscribe(event_type, attr)