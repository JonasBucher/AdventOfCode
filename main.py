import argparse
import importlib.util
import sys
import pathlib
from datetime import datetime, timedelta,timezone

def infer_defaults(day_arg: int | None, year_arg: int | None) -> tuple[int, int]:
    now = datetime.now(timezone.utc) - timedelta(hours=5)
    year = year_arg if year_arg is not None else now.year
    day = day_arg if day_arg is not None else (now.day if now.month == 12 else 1)
    return day, year

def resolve_path(day: int, year: int) -> tuple[pathlib.Path, pathlib.Path]:
    day_str = f"day{day:02d}"
    return pathlib.Path(__file__).parent / str(year) / day_str

def load_day_module(path: pathlib.Path):
    solution_path = path / "solution.py"
    mod_name = f"aoc_{solution_path.parent.parent.name}_{solution_path.parent.name}"
    spec = importlib.util.spec_from_file_location(mod_name, solution_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = module
    spec.loader.exec_module(module)
    return module

def read_input(path: pathlib.Path, sample: bool):
    path = path / "input.txt" if not sample else path / "sample.txt"
    return path.read_text(encoding="utf-8")

def run(year: int, day: int, part: int | None, sample: bool):
    path = resolve_path(day, year)
    module = load_day_module(path)
    raw = read_input(path, sample)
    parse_input = getattr(module, "parse_input", lambda r: r)
    data = parse_input(raw)

    def run_part(p: int):
        solver = getattr(module, f"solve_part{p}", None)
        return solver(data)

    parts = [part] if part else [1, 2]
    return {p: run_part(p) for p in parts}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int)
    parser.add_argument("--part", type=int, choices=[1, 2])
    parser.add_argument("--sample", action="store_true")
    parser.add_argument("--year", type=int)
    args = parser.parse_args()

    day, year = infer_defaults(args.day, args.year)
    results = run(year, day, args.part, args.sample)
    for p, value in results.items():
        print(f"{year} Day {day:02d} Part {p}: {value}")

if __name__ == "__main__":
    main()
