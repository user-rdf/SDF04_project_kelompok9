from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int = 0

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Product price cannot be negative")
        if self.stock < 0:
            raise ValueError("Product stock cannot be negative")
