# AAKI

**AAKI** (acronym for "Aplikacja Automatycznej Korekcji Interpunkcji") is an app to correct punctuation (mainly commas) in Polish texts. It is written in Python and uses Spacy for NLP.

## Installation

To run project locally, use:
```
git clone https://github.com/ack2406/aaki

cd aaki

pip install -r requirements.txt
```



To install the package, use:
```
pip install aaki
```

## Usage

If you want to play with the code, the best way is to create `.py` file inside `src` directory and use the code below.

```python
from aaki import CommaCorrector


corrector = CommaCorrector()

sentences = [
    "Ile dałbym by zapomnieć Cię.",
    "Wszystkie chwile te które są na nie."
    ]

corrector.correct(sentences)
```

## Tests

To run all tests, use:
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
