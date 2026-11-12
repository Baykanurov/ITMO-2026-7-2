import sys


def apply_discount(price: float, percent: float) -> float:
    """Цена со скидкой. percent — от 0 до 100."""
    return round(price * (1 - percent / 100), 2)


if __name__ == "__main__":
    price, percent = float(sys.argv[1]), float(sys.argv[2])
    print(apply_discount(price, percent))
