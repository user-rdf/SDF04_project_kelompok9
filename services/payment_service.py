class PaymentService:
    def charge(self, amount: float, payment_token: str) -> bool:
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero")
        if not payment_token:
            raise ValueError("Payment token is required")
        return True
