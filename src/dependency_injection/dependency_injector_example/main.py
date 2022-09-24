from pprint import pprint

from dependency_injector.wiring import Provide, inject  # noqa: F401

from dependency_injection.dependency_injector_example.assets import Reader
from dependency_injection.dependency_injector_example.containers import Container


@inject
def main(reader: Reader = Provide["reader"], path: str = Provide["path"]) -> None:
    pprint(reader.read(path))


# def main(reader: Reader, path: str) -> None:
#     pprint(reader.read(path))


if __name__ == "__main__":
    # https://github.com/ets-labs/python-dependency-injector/issues/339#issuecomment-747820448
    container = Container()
    container.wire(modules=[__name__])
    main()

    # container = Container()
    # main(container.reader(), container.path())
