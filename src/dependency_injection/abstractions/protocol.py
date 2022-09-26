from typing import Protocol


class Order:
    ...


class Save(Protocol):  # Explicit protocol, duck typing with types safety
    def save(self, order: Order) -> None:
        ...


class DbOrdersRepository(Save):  # Implements protocol
    def save(self, order: Order) -> None:
        print("Saving in db...")

    def a_method_that_does_not_belong_to_the_protocol(self) -> None:
        ...


class ShopCartService:
    def __init__(self, repository: Save) -> None:
        self._repository = repository

    def checkout(self) -> None:
        order = Order()

        self._repository.save(order)  # It’s certain that the object self._repository will have a save method
