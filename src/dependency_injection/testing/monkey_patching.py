from typing import Optional


class Order:
    def __init__(self) -> None:
        self.id: Optional[int] = None


class OrdersRepository:
    def save(self, order: Order) -> int:
        return 2


class ShopCartService:
    def __init__(self) -> None:
        self._repository = OrdersRepository()

    def checkout(self) -> int:
        order = Order()
        order.id = self._repository.save(order)
        return order.id
