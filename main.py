from models import Cart, Customer, Product
from services import OrderService, PricingService
from src.utils import format_currency


def main() -> None:
    product = Product(id=1, name="Keyboard", price=250_000, stock=10)
    cart = Cart()
    cart.add(product, quantity=2)

    pricing = PricingService(tax_rate=0.11, discount_rate=0.05)
    customer = Customer(id=1, name="Customer", email="customer@example.com")
    order = OrderService().create_order(customer, cart, payment_token="demo-token")

    print(f"Order #{order.id}: {order.status}")
    print(f"Total: {format_currency(pricing.total(cart))}")


if __name__ == "__main__":
    main()
