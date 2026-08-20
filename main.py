from events import Event, EventBus, EventListener, on_event
from repositories import Repository


class Foo: ...


class Bar: ...


class DummyFooEvent(Event[Foo]): ...


class DummyBarEvent(Event[Bar]): ...


e = EventBus()

e.subscribe_event(DummyFooEvent)
e.subscribe_event(DummyBarEvent)


class Listening(EventListener):
    @on_event(DummyFooEvent)
    def foo_event_handler(self, event: DummyFooEvent):
        print("Saw Foo")

    @on_event(DummyBarEvent)
    def bar_event_handler(self, event: DummyBarEvent):
        print("Saw Bar")

    @on_event(DummyBarEvent)
    def bar_event_handler_2(self, event: DummyBarEvent):
        print("bar bar")


class Listening2(EventListener):
    @on_event(DummyFooEvent)
    def foo_event_handler(self, event: DummyFooEvent):
        print("Saw Foo Listening2")

    @on_event(DummyBarEvent)
    def bar_event_handler(self, event: DummyBarEvent):
        print("Saw Bar Listening2")

    @on_event(DummyBarEvent)
    def bar_event_handler_2(self, event: DummyBarEvent):
        print("bar bar Listening2")


l = Listening(e)
l2 = Listening2(e)
e.publish(DummyBarEvent(Bar()))
e.publish(DummyFooEvent(Foo()))

r: Repository[Foo] = Repository()
