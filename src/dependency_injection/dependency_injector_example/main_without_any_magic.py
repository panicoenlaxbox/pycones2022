from pprint import pprint

from dependency_injection.dependency_injector_example.assets import Reader
from dependency_injection.dependency_injector_example.containers import Container


def main(reader: Reader, path: str) -> None:
    pprint(reader.read(path))


if __name__ == "__main__":
    container = Container()
    main(container.reader(), container.path())
