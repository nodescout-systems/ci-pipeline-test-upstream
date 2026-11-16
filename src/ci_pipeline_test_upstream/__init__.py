"""A small package that stands in for an upstream project in tests of manual forks."""

import sys

__all__ = ["greet", "main"]

USAGE = "usage: ci-pipeline-test-upstream NAME"


def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}."


def main(argv: list[str] | None = None) -> int:
    """Print a greeting for the one name given, and refuse anything else."""
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1 or args[0].startswith("-"):
        print(USAGE, file=sys.stderr)
        return 2
    print(greet(args[0]))
    return 0
