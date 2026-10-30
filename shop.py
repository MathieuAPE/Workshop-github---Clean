def apply_discount(total):
    """10% de remise a partir de 100 euros."""
    if total >= 100:
        return total * 0.9
    return total


def add_tax(total, rate=0.2):
    return total * (1 + rate)
