# ruff: noqa

from events import Event, EventBus


class Foo: ...
class Bar: ...


class DummyFooEvent(Event[Foo]): ...
class DummyBarEvent(Event[Bar]): ...


e = EventBus()

e.subscribe_event(DummyFooEvent)
e.subscribe_event(DummyBarEvent)


@e.on(DummyFooEvent)
def FooEventHandler(event: DummyFooEvent):
    print("Saw Foo")


@e.on(DummyBarEvent)
def BarEventHandler(event: DummyBarEvent):
    print("Saw Bar")


e.publish(DummyBarEvent(Bar()))
e.publish(DummyFooEvent(Foo()))
