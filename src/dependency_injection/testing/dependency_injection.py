import abc
from typing import Optional


class Order:
    def __init__(self) -> None:
        self.id: Optional[int] = None


class OrdersRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, order: Order) -> int:
        ...


class DbOrdersRepository(OrdersRepository):
    def save(self, order: Order) -> int:
        return 2


class ShopCartService:
    def __init__(self, repository: OrdersRepository):
        self._repository = repository

    def checkout(self) -> int:
        order = Order()
        order.id = self._repository.save(order)
        return order.id
