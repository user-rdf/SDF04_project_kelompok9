def validate_name(name: str) -> bool:
    if not name or not name.strip():
        return False
    return len(name.strip()) >= 3