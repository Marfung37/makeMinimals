# makeMinimals
Pulls the fumen from the output of [sfinder-strict-minimal](https://github.com/eight04/sfinder-strict-minimal) and gives a tinyurl to the minimals.

# Usage
```bash
python makeMinimals.py
```
This outputs a tinyurl to stdout.

This assumes there's a `path_minimal_strict.md` file in the current directory from running
```bash
sfinder-minimal path.csv
```
The sfinder-minimal command is from [sfinder-strict-minimal](https://github.com/eight04/sfinder-strict-minimal).
