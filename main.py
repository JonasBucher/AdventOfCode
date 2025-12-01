import argparse
import importlib
import pathlib

ROOT = pathlib.Path(__file__).parent
DAYS_DIR = ROOT / "days"


def load_day_module(day_number: int):
    day_str = f"day{day_number:02d}"
    module_name = f"days.{day_str}.solution"
    return importlib.import_module(module_name)


def read_input(day_number: int, sample: bool = False) -> str:
    day_str = f"day{day_number:02d}"
    path = DAYS_DIR / day_str / ("sample.txt" if sample else "input.txt")
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    return path.read_text(encoding="utf-8")


def run(day: int, part: int | None, sample: bool):
    module = load_day_module(day)
    raw = read_input(day, sample)
    parse_input = getattr(module, "parse_input", lambda r: r)
    data = parse_input(raw)

    def run_part(p: int):
        solver = getattr(module, f"solve_part{p}", None)
        if solver is None:
            raise AttributeError(f"solve_part{p} not implemented for day {day}")
        return solver(data)

    parts = [part] if part else [1, 2]
    results = {}
    for p in parts:
        results[p] = run_part(p)
    return results


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code 2025 solutions")
    parser.add_argument("day", type=int, help="Day number (1-12)")
    parser.add_argument("--part", type=int, choices=[1, 2], help="Specific part to run")
    parser.add_argument("--sample", action="store_true", help="Use sample input instead of puzzle input")
    args = parser.parse_args()

    results = run(args.day, args.part, args.sample)
    for p, value in results.items():
        print(f"Day {args.day:02d} Part {p}: {value}")


if __name__ == "__main__":
    main()
