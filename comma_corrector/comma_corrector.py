from spacy import load, Language
import re

import comma_corrector.rules as rules


class CommaCorrector:
    """
    Corrects punctuation in given sentence.
    """

    def __init__(self, sentence: str = "") -> None:
        self._nlp: Language = load("pl_core_news_sm")

        self._sentence: str = sentence
        self._sentence_doc: Language = self.create_doc(self._sentence)

        # get all rules from rules.py
        self._rules: dict = {rule[6:]: getattr(rules, rule) for rule in dir(
            rules) if rule.startswith('check_')}

        # get all keys from rules dict
        self._rules_keys: list[str] = [key for key in self._rules.keys()]

    @property
    def sentence(self) -> str:
        return self._sentence

    @sentence.setter
    def sentence(self, sentence: str) -> None:
        self._sentence = sentence
        self._sentence_doc = self.create_doc(self._sentence)

    @property
    def sentence_doc(self) -> Language:
        return self._sentence_doc

    def _join_sentence(self, sentence: list[str]) -> str:
        sentence = ' '.join(sentence)

        sentence = re.sub(r' ([.,?!:;])', r'\1', sentence)

        return sentence

    def create_doc(self, sentence: str) -> Language:
        return self._nlp(sentence)

    def correct(self) -> str:
        sentence_text: list[str] = [token.text for token in self._sentence_doc]
        shift: int = 0

        occured: dict[str, bool] = {key: False for key in self._rules_keys}

        for token in self._sentence_doc:
            index = token.i

            if index == 0:
                continue

            if token.text not in self._rules_keys:
                continue

            result = self._rules[token.text](
                token, self._sentence_doc[index - 1], occured[token.text])

            occured[token.text] = result['occured']

            if not result['insert']:
                continue

            sentence_text.insert(index + result['insert_pos'], ',')

            shift += 1

        return self._join_sentence(sentence_text)
