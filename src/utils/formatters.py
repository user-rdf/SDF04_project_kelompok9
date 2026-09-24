def format_currency(amount: float, currency: str = "Rp") -> str:
    return f"{currency} {amount:,.2f}"
