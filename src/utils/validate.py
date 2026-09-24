def validate_name(name: str) -> bool:
    """Memvalidasi bahwa nama tidak kosong dan minimal 3 karakter"""
    return bool(name and len(name.strip()) >= 3)