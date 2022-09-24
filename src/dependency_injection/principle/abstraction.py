from abc import ABC, abstractmethod


class Reader(ABC):  # Abstraction
    @abstractmethod
    def read(self) -> str:
        ...
