# Advent of Code Runner

This repo uses a strict year/day structure for solutions and inputs.

## Structure

- `main.py`: CLI runner
- `<year>/dayXX/`: solution folder for a given year and day
	- `solution.py`: implementation with `parse_input`, `solve_part1`, `solve_part2`
	- `input.txt`: puzzle input
	- `sample.txt`: sample input (optional)

Example:

```
2025/
	day01/
		solution.py
		input.txt
		sample.txt
```

## Usage

- Inferred year/day (UTC-5), run both parts:

```powershell
python main.py
```

- Explicit day and part (year inferred):

```powershell
python main.py 2 --part 2
```

- Explicit year (day inferred):

```powershell
python main.py --year 2025
```

- Use sample input:

```powershell
python main.py 1 --sample --year 2025
```

Notes:
- Defaults use current date in UTC-5 (AoC timezone). If not December, default day is 1.
- Runner only supports the strict structure `ROOT/<year>/dayXX/`.


Happy coding!