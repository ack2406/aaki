from spacy import Language, tokens

from . import rules as rls
from .comma_corrector import CommaCorrector


class CommaTester:
    """
    Tester for single sentence punctuation.
    Takes correct sentence as input,
    transforms it to sentence without commas
    and checks if checker returns correct result.
    """

    def __init__(self, sentences: list[str] = []):
        self._corrector: CommaCorrector = CommaCorrector()
        self._sentences: list[str] = sentences

    def _rate_sentence(self, corrected_doc: Language, sentences_doc: Language) -> dict[str, int]:
        """
        Rates correctness of corrected sentence.
        """

        # create index for both documents
        sentences_pos: int = 0
        corrected_pos: int = 0

        # create dict for points
        points: dir[str, int] = {"correct": 0, "incorrect": 0, "missing": 0}

        # iterate through both documents
        while sentences_pos < len(sentences_doc) and corrected_pos < len(corrected_doc):
            # get tokens
            sentences_token: tokens.token.Token = sentences_doc[sentences_pos]
            corrected_token: tokens.token.Token = corrected_doc[corrected_pos]

            # if both tokens are commas, add point to correct
            if sentences_token.text == ',' and corrected_token.text == ',':
                points["correct"] += 1
            # if token in sentences is comma and token in corrected is not, add point to missing
            elif sentences_token.text == ',' and corrected_token.text != ',':
                points["missing"] += 1
                corrected_pos -= 1
            # if token in sentences is not comma and token in corrected is, add point to incorrect
            elif sentences_token.text != ',' and corrected_token.text == ',':
                points["incorrect"] += 1
                sentences_pos -= 1

            # increment both indexes
            sentences_pos += 1
            corrected_pos += 1

        return points

    def _rate(self, corrected_docs: Language, sentences_docs: Language) -> dict[str, int]:
        """
        Rates correctness of corrected sentences.
        """

        points: dict[str, int] = {"correct": 0, "incorrect": 0, "missing": 0}
        corrected_docs = list(corrected_docs)
        sentences_docs = list(sentences_docs)

        for corrected_doc, sentences_doc in zip(list(corrected_docs), list(sentences_docs)):
            result = self._rate_sentence(corrected_doc, sentences_doc)
            points["correct"] += result["correct"]
            points["incorrect"] += result["incorrect"]
            points["missing"] += result["missing"]

        return points

    def test(self, sentences: list[str] = []) -> dict[str, int]:
        # transform sentences to sentences without commas
        no_commas_sentences: list[str] = [
            sentence.replace(',', '') for sentence in sentences]

        # correct sentence and get result
        corrected_sentences: str = self._corrector.correct(no_commas_sentences)

        corrected_docs: Language = self._corrector.create_docs(
            corrected_sentences)
        sentences_doc = self._corrector.create_docs(sentences)

        # return rated result in format {'correct': int, 'incorrect': int, 'missing': int}
        return self._rate(corrected_docs, sentences_doc)

    def test_distinct(self, sentences: list[str] = []) -> dict[str, dict[str, int]]:
        """
        Tests distinct rules.
        """

        rules = {rule[6:]: getattr(rls, rule) for rule in dir(rls) if rule.startswith('check_')}

        rules_points = {}

        for key, value in rules.items():
            # create list of sentences that contain rule as a word
            sentences_with_rule = [sentence for sentence in sentences if key in sentence.split(" ")]

            # if there are no sentences with rule, skip
            if sentences_with_rule == []:
                continue
            
            # set rule to be checked
            self._corrector.rules = {key: value}

            rules_points[key] =  self.test(sentences_with_rule)
        return rules_points
