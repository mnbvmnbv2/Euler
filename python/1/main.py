def main(up_to: int = 1000) -> int:
    """Multiples of 3 and 5

    Args:
        up_to (int, optional): Number to calculate up to. Defaults to 1000.

    Returns:
        int: Sum of all multiples of 3 and 5 up to `up_to`
    """
    return sum([i for i in range(up_to) if (i % 5 == 0 or i % 3 == 0)])
