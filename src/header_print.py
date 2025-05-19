def header_print(header: str) -> None:
    """Print the provided `header` in a nice format.

    Example: `header_print("Exercise 1.3")` prints like:

    Exercise 1.3
    ============

    :param header: The header to print nicely.
    """
    print(f"\n{header}\n{'=' * len(header)}")
