    value = sign * int(digits) if digits else 0
    value = max(-2**63, min(value, 2**63 - 1))
    value &= 0xFFFFFFFF
    return value - 2**32 if value >= 2**31 else value
