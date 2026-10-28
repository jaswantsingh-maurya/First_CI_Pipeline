# Assignment 4 — Python CI Pipeline with GitHub Actions

[![Python CI](https://github.com/mhatreanuj57-alt/First_CI_Pipeline/actions/workflows/python-ci.yml/badge.svg)](https://github.com/mhatreanuj57-alt/First_CI_Pipeline/actions/workflows/python-ci.yml)

Build ten beginner-friendly Python algorithms and verify them with pytest locally
and automatically on GitHub. Each program is added in its own commit, after the
previous program passes CI.

Repository: [First_CI_Pipeline](https://github.com/mhatreanuj57-alt/First_CI_Pipeline)

## Technologies

Python 3.12 or newer, pytest, Git, and GitHub Actions on Ubuntu.

## Programs 21–30

| No. | Function | Purpose |
| --- | --- | --- |
| 21 | `largest_word(sentence)` | Longest word; strip surrounding punctuation; first wins ties |
| 22 | `is_anagram(first, second)` | Compare letters ignoring case and spaces |
| 23 | `bubble_sort(numbers)` | Return a new ascending list using bubble sort |
| 24 | `merge_sorted_lists(list1, list2)` | Merge two sorted lists |
| 25 | `find_max_min(numbers)` | Return maximum and minimum; reject an empty list |
| 26 | `sum_of_list(numbers)` | Accumulate list elements with a loop |
| 27 | `rotate_list(items, k)` | Rotate right; negative positions rotate left |
| 28 | `set_intersection(first, second)` | Return common set elements |
| 29 | `is_armstrong(number)` | Check digit powers; negative numbers return false |
| 30 | `decimal_to_binary(number)` | Convert by repeated division; reject negative numbers |

## Final project structure

```text
First_CI_Pipeline/
├── .github/workflows/python-ci.yml
├── codes/
│   ├── 21_largest_word.py
│   ├── 22_anagram_strings.py
│   ├── 23_sort_without_sort.py
│   ├── 24_merge_sorted_lists.py
│   ├── 25_max_min_list.py
│   ├── 26_sum_of_list.py
│   ├── 27_rotate_list.py
│   ├── 28_set_intersection.py
│   ├── 29_armstrong_number.py
│   └── 30_decimal_to_binary.py
├── test_cases/                 # One corresponding test_<program>.py per program
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Local setup and tests

```sh
git clone https://github.com/mhatreanuj57-alt/First_CI_Pipeline.git
cd First_CI_Pipeline
python -m venv .venv
```

Activate on PowerShell with `.venv\Scripts\Activate.ps1`, on Windows Command
Prompt with `.venv\Scripts\activate`, or on Linux/macOS with
`source .venv/bin/activate`.

```sh
python -m pip install -r requirements.txt
python -m pytest -v
python -m pytest -v test_cases/test_21_largest_word.py
```

`pytest.ini` adds `codes` to the import path and discovers tests in `test_cases`.
Tests use `importlib.import_module()` because program filenames begin with digits.
The local `.venv`, Python bytecode, and pytest cache are ignored by Git.

## CI pipeline

The `Python CI` workflow runs on pushes to `main` and pull requests targeting
`main`. A fresh `ubuntu-latest` runner checks out the repository, installs Python
3.12, installs `requirements.txt`, and runs pytest. A failed test fails the job;
all passing tests produce a green success status in the Actions tab.

Program 21 and the initial configuration are pushed first. The workflow is added
in a separate commit. Programs 22–30 are then tested, committed, and pushed one
at a time, waiting for GitHub to confirm success before starting the next program.
Assignment 4: Python CI pipeline with GitHub Actions and pytest
