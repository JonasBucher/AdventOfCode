# AdventOfCode2025

Project scaffold for the first 12 Advent of Code 2025 challenges in Python.

## Structure

```
days/
	day01/solution.py input.txt sample.txt
	...
	day12/solution.py input.txt sample.txt
main.py
.gitignore
```

Each `solution.py` defines:

```python
def parse_input(raw: str): ...
def solve_part1(data): ...
def solve_part2(data): ...
```

`input.txt` should contain your puzzle input (not committed until filled). `sample.txt` can hold the sample from the problem statement.

## Running

From the repository root:

```powershell
python main.py 1            # Run Day 1 both parts with real input
python main.py 1 --sample   # Run Day 1 using sample.txt
python main.py 5 --part 2   # Run only Part 2 for Day 5
```

## Adding Solutions

Replace the `TODO` comments in each `solve_part1` / `solve_part2` with your implementation. Use `parse_input` to transform the raw text into convenient data structures.

## Notes

- Extend beyond Day 12 by copying an existing day directory and incrementing the number.
- Consider adding tests (e.g. with `pytest`) for tricky parsing or logic.
- Keep inputs private; avoid committing actual puzzle inputs if desired.

Happy coding!