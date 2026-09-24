import unittest

from models import Cart, Product
from services import PricingService


class PricingServiceTests(unittest.TestCase):
    def test_total_applies_discount_then_tax(self) -> None:
        cart = Cart()
        cart.add(Product(1, "Keyboard", 100.0), 2)
        pricing = PricingService(tax_rate=0.1, discount_rate=0.2)

        self.assertEqual(pricing.subtotal(cart), 200.0)
        self.assertEqual(pricing.discount(cart), 40.0)
        self.assertEqual(pricing.tax(cart), 16.0)
        self.assertEqual(pricing.total(cart), 176.0)


if __name__ == "__main__":
    unittest.main()
