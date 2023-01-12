# AAKI

**AAKI** (acronym for "Aplikacja Automatycznej Korekcji Interpunkcji") is an app to correct punctuation (mainly commas) in Polish texts. It is written in Python and uses Spacy for NLP.

## Installation

```
pip install aaki
```

## Usage

```python
from aaki import CommaCorrector


corrector = CommaCorrector()

corrector.sentences = [
    "Ile dałby by zapomnieć Cię.",
    "Wszystkie chwile te które są na nie."
    ]

corrector.run()
```

## Tests

```
pytest
```

To run specific tests, use `pytest -k`:

```
pytest -k test_<rule>
```

For example, to run tests for the rule `ponieważ`, use:

```
pytest -k test_ponieważ
```
