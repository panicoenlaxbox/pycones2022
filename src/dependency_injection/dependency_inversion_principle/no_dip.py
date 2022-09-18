class Order:
    ...


class OrdersRepository:  # Low-level module
    def save(self, order: Order) -> None:
        ...


class ShopCartService:  # High-level module
    def checkout(self) -> None:
        order = Order()

        repository = OrdersRepository()  # High-level module depends on a low-level module
        repository.save(order)
