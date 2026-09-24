from dataclasses import dataclass, field
from datetime import datetime

from .customer import Customer
from .product import Product


@dataclass
class OrderItem:
    product: Product
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price


@dataclass
class Order:
    id: int
    customer: Customer
    items: list[OrderItem] = field(default_factory=list)
    status: str = "pending"
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.items)
