from models.cart import Cart


class PricingService:
    def __init__(self, tax_rate: float = 0.0, discount_rate: float = 0.0) -> None:
        if not 0 <= tax_rate <= 1 or not 0 <= discount_rate <= 1:
            raise ValueError("Rates must be between 0 and 1")
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate

    def subtotal(self, cart: Cart) -> float:
        return round(cart.total(), 2)

    def discount(self, cart: Cart) -> float:
        return round(self.subtotal(cart) * self.discount_rate, 2)

    def tax(self, cart: Cart) -> float:
        taxable_amount = self.subtotal(cart) - self.discount(cart)
        return round(taxable_amount * self.tax_rate, 2)

    def total(self, cart: Cart) -> float:
        return round(self.subtotal(cart) - self.discount(cart) + self.tax(cart), 2)
