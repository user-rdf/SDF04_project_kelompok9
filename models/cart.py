from dataclasses import dataclass, field

from .product import Product


@dataclass
class CartItem:
    product: Product
    quantity: int

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

    @property
    def subtotal(self) -> float:
        return self.product.price * self.quantity


@dataclass
class Cart:
    items: list[CartItem] = field(default_factory=list)

    def add(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def total(self) -> float:
        return sum(item.subtotal for item in self.items)
