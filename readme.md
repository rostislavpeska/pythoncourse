# Python Training Playground

This repository collects the exercises used during a Python training course. It is not a single runnable application; instead it contains small, focused scripts that demonstrate core Python concepts, object-oriented programming, error handling, simple data processing, unit testing, and a few design patterns.

## Highlights
- Object-oriented modelling of a small `DogShelter`/`Zoo` domain (`animal.py`, `dog.py`, `cat.py`, `dogshelter.py`, `zoo.py`) complete with custom exceptions and basic logging.
- Introductory design-pattern examples such as Singleton, Factory, Builder, and a hand-written decorator pattern (`design_patterns.py`, `decorator.py`).
- Snippets that touch on standard-library tooling: exception handling (`exceptions.py`), file IO (`read.py`), and SQLite usage (`database_communication.py`).
- A minimal `pytest` test module (`test/test.py`) showing how to structure and assert simple unit tests.
- `model_api/models/` holds pre-trained pickle files that can be loaded from other notebooks or scripts during the course.

## Running the examples
Create a virtual environment, install the dependencies listed in `requierments.txt`, and then execute whichever script you want to explore.

```bash
python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
pip install -r requierments.txt
python opp1.py             # sample run of the OOP shelter example
pytest                     # run the sample tests
```

## Notes
- Most scripts are self-contained: run them directly with `python <file.py>` to see the output that was discussed during training.
- `database_communication.py` writes to `tutorial.db` in the working directory; delete that file if you need a fresh start.
- `read.py` expects `username.csv` to exist in the repository root when the pandas example is executed.
