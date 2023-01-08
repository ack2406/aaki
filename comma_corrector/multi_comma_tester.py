from comma_corrector.comma_corrector import CommaCorrector
from comma_corrector.multi_comma_corrector import MultiCommaCorrector
from comma_corrector.comma_tester import CommaTester
from spacy import Language


class MultiCommaTester:
    """
    Tester for multiple sentences punctuation.
    """

    def __init__(self):
        self._corrector: CommaCorrector = CommaCorrector()
        self._multi_corrector: MultiCommaCorrector = MultiCommaCorrector()
        self._tester: CommaTester = CommaTester()
        self._data: list[str] = []

    @property
    def data(self) -> list[str]:
        return self._data

    @data.setter
    def data(self, data: list[str]) -> None:
        self._data = data

    def _rate(self, corrected_docs: list[Language], data_docs: list[Language]) -> dict[str, int]:
        """
        Rates correctness of corrected sentences.

        """
        points: dict[str, int] = {"correct": 0, "incorrect": 0, "missing": 0}

        for corrected_doc, data_doc in zip(corrected_docs, data_docs):
            result = self._tester._rate(corrected_doc, data_doc)
            points["correct"] += result["correct"]
            points["incorrect"] += result["incorrect"]
            points["missing"] += result["missing"]

        return points

    def test(self) -> dict[str, int]:
        """
        Tests correctness of comma corrector.
        """

        # transform sentences to sentences without commas
        no_commas_sentences = [sentence.replace(
            ",", "") for sentence in self._data]

        # set sentences and sentences_docs in corrector
        self._multi_corrector.sentences = no_commas_sentences
        self._multi_corrector.sentences_doc = self._multi_corrector.create_docs(
            no_commas_sentences)

        # correct sentences
        corrected_sentences = self._multi_corrector.correct()

        # create spaCy documents from corrected sentences
        corrected_docs = self._corrector.create_docs(corrected_sentences)

        # create spaCy documents from data
        data_docs = self._corrector.create_docs(self._data)

        # rate correctness of corrected sentences
        return self._rate(corrected_docs, data_docs)
