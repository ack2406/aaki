from comma_corrector.comma_corrector import CommaCorrector
from spacy import Language


class MultiCommaCorrector:
    """
    Corrects punctuation in given sentence.
    """

    def __init__(self, sentences: list[str] = []) -> None:
        self._corrector: CommaCorrector = CommaCorrector()
        self._sentences: list[str] = sentences
        self._sentences_doc: list[Language] = []

    @property
    def sentences(self) -> list[str]:
        return self._sentences

    @sentences.setter
    def sentences(self, sentences: list[str]) -> None:
        self._sentences = sentences

    def create_docs(self, sentences) -> None:
        """Creates spaCy documents from given sentences."""
        return self._corrector.create_docs(sentences)

    @property
    def sentences_doc(self) -> list[Language]:
        return self._sentences_doc

    @sentences_doc.setter
    def sentences_doc(self, sentences_doc: list[Language]) -> None:
        self._sentences_doc = sentences_doc

    def correct(self) -> list[str]:
        corrected_sentences: list[str] = []

        for sentence, sentence_doc in zip(self._sentences, self._sentences_doc):
            self._corrector.sentence = sentence
            self._corrector.sentence_doc = sentence_doc
            corrected_sentences.append(self._corrector.correct())

        return corrected_sentences
