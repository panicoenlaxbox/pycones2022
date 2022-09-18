from unittest.mock import create_autospec, patch

from assertpy import assert_that

from dependency_injection.testing.monkey_patching import OrdersRepository, ShopCartService


def test_monkey_patching() -> None:
    mock_orders_repository_instance = create_autospec(spec=OrdersRepository, spec_set=True, instance=True)
    mock_orders_repository_instance.save.return_value = 1
    with patch("dependency_injection.testing.monkey_patching.OrdersRepository") as mock_orders_repository:
        mock_orders_repository.return_value = mock_orders_repository_instance
        service = ShopCartService()

        actual = service.checkout()

        assert_that(actual).is_equal_to(1)
