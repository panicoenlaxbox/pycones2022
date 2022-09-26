# flake8: noqa
class Order:
    pass


class StockAllocator:
    pass


class PriceCalculator:
    pass


class CustomerScoreChecker:
    pass


class MailSender:
    pass


class OrderAllocator:
    def __init__(self) -> None:
        ...

    def allocate(self, order: Order) -> None:
        stock_allocator = StockAllocator()
        price_calculator = PriceCalculator()
        customer_score_checker = CustomerScoreChecker()
        mail_sender = MailSender()


class OtherAllocator2:
    def __init__(
        self,
        stock_allocator: StockAllocator,
        price_calculator: PriceCalculator,
        customer_score_checker: CustomerScoreChecker,
        main_sender: MailSender,
    ) -> None:
        self._stock_allocator = stock_allocator
        self._price_calculator = price_calculator
        self._customer_score_checker = customer_score_checker
        self._main_sender = main_sender

    def allocate(self, order: Order) -> None:
        ...
