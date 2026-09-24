from models.product import Product


class InventoryService:
    def reserve(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if product.stock < quantity:
            raise ValueError(f"Insufficient stock for {product.name}")
        product.stock -= quantity

    def restock(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        product.stock += quantity
