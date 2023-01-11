# AAKI

**AAKI** (acronym for "Aplikacja Automatycznej Korekcji Interpunkcji") is an app to correct punctuation (mainly commas) in Polish texts. It is written in Python and uses Spacy for NLP.

## Installation

For now, there is no pip package, so you have to clone the repo and install the requirements manually.

```
git clone https://github.com/ack2406/aaki
cd aaki
pip install -r requirements.txt
```

# Tests

To run tests, use `pytest`:

```
pytest
```

To run specific tests, use `pytest -k`:

```
pytest -k test_aby
pytest -k test_oraz
pytest -k test_ale
```

