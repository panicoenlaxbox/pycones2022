# region Classes
class Foo:
    ...


class Bar:
    ...


class Baz:
    ...


class Qux:
    ...


class Quux:
    ...


# endregion


class Corge:
    def __init__(self) -> None:  # Code smell?
        self._foo = Foo()
        self._bar = Bar()
        self._baz = Baz()
        self._qux = Qux()
        self._quux = Quux()


class CorgeDI:
    def __init__(self, foo: Foo, bar: Bar, baz: Baz, qux: Qux, quux: Quux) -> None:  # Code smell
        ...
