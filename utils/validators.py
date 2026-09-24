import re


_EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email: str) -> bool:
    return bool(_EMAIL_PATTERN.fullmatch(email))


def is_positive_quantity(quantity: int) -> bool:
    return isinstance(quantity, int) and quantity > 0
