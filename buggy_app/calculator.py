"""Calculator functions. Contains an intentional bug for debugger testing."""


def calculate_average(numbers: list[float]) -> float:
    """Return the average of numbers.

    BUG: This function does not handle an empty list.
    """
    return sum(numbers) / len(numbers)
