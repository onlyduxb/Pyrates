# ruff: noqa

from events import Event, EventBus, EventListener, on_event


class Foo: ...
class Bar: ...


class DummyFooEvent(Event[Foo]): ...
class DummyBarEvent(Event[Bar]): ...


e = EventBus()

e.subscribe_event(DummyFooEvent)
e.subscribe_event(DummyBarEvent)

class Listening(EventListener):
    @on_event(DummyFooEvent)
    def FooEventHandler(self, event: DummyFooEvent):
        print("Saw Foo")


    @on_event(DummyBarEvent)
    def BarEventHandler(self, event: DummyBarEvent):
        print("Saw Bar")

l = Listening(e)
e.publish(DummyBarEvent(Bar()))
e.publish(DummyFooEvent(Foo()))
