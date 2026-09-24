from models.cart import Cart
from models.customer import Customer
from models.order import Order, OrderItem

from .inventory_service import InventoryService
from .payment_service import PaymentService


class OrderService:
    def __init__(self, inventory: InventoryService | None = None, payment: PaymentService | None = None) -> None:
        self.inventory = inventory or InventoryService()
        self.payment = payment or PaymentService()
        self._next_id = 1

    def create_order(self, customer: Customer, cart: Cart, payment_token: str) -> Order:
        if not cart.items:
            raise ValueError("Cannot create an order from an empty cart")

        for item in cart.items:
            self.inventory.reserve(item.product, item.quantity)

        order = Order(
            id=self._next_id,
            customer=customer,
            items=[OrderItem(item.product, item.quantity, item.product.price) for item in cart.items],
        )
        self.payment.charge(order.total, payment_token)
        order.status = "paid"
        self._next_id += 1
        return order
