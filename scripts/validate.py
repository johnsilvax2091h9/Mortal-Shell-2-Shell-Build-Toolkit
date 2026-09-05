# Build: 5ea0bf2d426654482659a7e878a1a70b

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
