from unittest.mock import create_autospec

from assertpy import assert_that

from dependency_injection.testing.dependency_injection import OrdersRepository, ShopCartService


def test_mocking() -> None:
    mock_orders_repository = create_autospec(spec=OrdersRepository, spec_set=True, instance=True)
    mock_orders_repository.save.return_value = 1
    service = ShopCartService(mock_orders_repository)

    actual = service.checkout()

    assert_that(actual).is_equal_to(1)
