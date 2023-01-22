# AAKI

**AAKI** (acronym for "Aplikacja Automatycznej Korekcji Interpunkcji") is an app to correct punctuation (mainly commas) in Polish texts. It is written in Python and uses Spacy for NLP.

## Installation

To run project locally, use:

```bash
git clone https://github.com/ack2406/aaki

cd aaki

pip install -r requirements.txt
```

If you want to play with the code, run `example.py`:

```bash
python3 src/example.py
```

To install the package, use:

```bash
pip install aaki
```

## Usage

```python
from aaki import CommaCorrector


corrector = CommaCorrector()

sentences = [
    "Ile dałbym by zapomnieć Cię.",
    "Wszystkie chwile te które są na nie."
    ]

corrected_sentences = corrector.correct(sentences)

print(corrected_sentences)
```

## Tests

To run all tests, use:

```bash
pytest
```

To run specific tests, use `pytest -k`:

```bash
pytest -k test_<rule>
```

For example, to run tests for the rule `ponieważ`, use:

```bash
pytest -k test_ponieważ
```
