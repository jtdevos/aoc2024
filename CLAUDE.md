# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Advent of Code 2024 solutions repository containing Python implementations for daily programming challenges. Each day's solution is contained in its own directory (`day01/`, `day02/`, etc.) with a `main.py` file and `resources/` folder containing input files.

## Development Environment

- **Python Version**: 3.13 (specified in Pipfile)
- **Package Manager**: Pipenv
- **Dependencies**: ipython for interactive development

## Common Commands

### Environment Setup
```bash
# Install dependencies
pipenv install

# Activate virtual environment
pipenv shell
```

### Running Solutions
```bash
# Run a specific day's solution
cd day01 && python main.py

# Run from project root
python day01/main.py
```

### Interactive Development
```bash
# Start IPython for interactive testing
ipython
```

## Code Architecture

### File Structure Pattern
Each day follows this structure:
- `dayXX/main.py` - Contains the solution logic
- `dayXX/resources/sample.txt` - Sample input for testing
- `dayXX/resources/input.txt` - Actual puzzle input

### Common Patterns
- **Input Reading**: Most solutions use a `read_lines(path)` helper function to read and strip input files
- **Two-Part Solutions**: Many days have `part1()` and `part2()` functions, or `main()` and `main2()` functions
- **Data Parsing**: Solutions often parse input into structured data (lists of numbers, rules, etc.)
- **File Paths**: Solutions use relative paths like `'resources/sample.txt'` and `'resources/input.txt'`

### Solution Style
- Functions are often defined at module level with descriptive names
- Debug printing is common for development (many `print()` statements)
- Solutions typically test against sample input first, then run on actual input
- Code style is informal/competitive programming oriented rather than production code