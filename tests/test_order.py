import unittest

from models import Cart, Customer, Product
from services import OrderService


class OrderServiceTests(unittest.TestCase):
    def test_create_paid_order_reduces_stock(self) -> None:
        product = Product(1, "Mouse", 50.0, stock=3)
        cart = Cart()
        cart.add(product, 2)

        order = OrderService().create_order(Customer(1, "Ari", "ari@example.com"), cart, "token")

        self.assertEqual(order.status, "paid")
        self.assertEqual(order.total, 100.0)
        self.assertEqual(product.stock, 1)

    def test_empty_cart_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            OrderService().create_order(Customer(1, "Ari", "ari@example.com"), Cart(), "token")


if __name__ == "__main__":
    unittest.main()
