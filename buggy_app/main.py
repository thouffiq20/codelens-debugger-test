"""Run the first intentional failure for CodeLens AI Debugger testing."""

from buggy_app.calculator import calculate_average


def main() -> None:
    sample_numbers: list[float] = []
    print("Average:", calculate_average(sample_numbers))


if __name__ == "__main__":
    main()
