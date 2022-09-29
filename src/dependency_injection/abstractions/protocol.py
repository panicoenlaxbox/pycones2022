from typing import Protocol


class Order:
    ...


class Save(Protocol):  # Explicit protocol, statick duck typing, type safety
    def save(self, order: Order) -> None:
        ...


class DbOrdersRepository(Save):  # Implements protocol
    def save(self, order: Order) -> None:
        print("Saving in db...")

    def a_method_that_has_nothing_to_do_with_the_protocol(self) -> None:
        ...


class ShopCartService:
    def __init__(self, repository: Save) -> None:
        self._repository = repository

    def checkout(self) -> None:
        order = Order()

        self._repository.save(order)  # It’s certain that self._repository will have a save method
