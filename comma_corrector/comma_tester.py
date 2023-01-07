from comma_corrector.comma_corrector import CommaCorrector
from spacy import Language, tokens


class CommaTester:
    """
    Tester for single sentence punctuation.
    Takes correct sentence as input,
    transforms it to sentence without commas
    and checks if checker returns correct result.
    """

    def __init__(self):
        self.corrector: CommaCorrector = CommaCorrector()
        self._data: str = ""

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, data: str) -> None:
        self._data = data

    def _rate(self, corrected_sentence: str) -> dict[str, int]:
        """
        Rates correctness of corrected sentence.
        """

        # create spaCy documents
        data_doc: Language = self.corrector.create_doc(self._data)
        corrected_doc: Language = self.corrector.create_doc(corrected_sentence)

        # create index for both documents
        data_pos: int = 0
        corrected_pos: int = 0

        # create dict for points
        points: dir[str, int] = {"correct": 0, "incorrect": 0, "missing": 0}

        # iterate through both documents
        while data_pos < len(data_doc) and corrected_pos < len(corrected_doc):
            # get tokens
            data_token: tokens.token.Token = data_doc[data_pos]
            corrected_token: tokens.token.Token = corrected_doc[corrected_pos]

            # if both tokens are commas, add point to correct
            if data_token.text == ',' and corrected_token.text == ',':
                points["correct"] += 1
            # if token in data is comma and token in corrected is not, add point to missing
            elif data_token.text == ',' and corrected_token.text != ',':
                points["missing"] += 1
                corrected_pos -= 1
            # if token in data is not comma and token in corrected is, add point to incorrect
            elif data_token.text != ',' and corrected_token.text == ',':
                points["incorrect"] += 1
                data_pos -= 1

            # increment both indexes
            data_pos += 1
            corrected_pos += 1

        return points

    def test(self) -> dict[str, int]:
        # transform sentence to sentence without commas for testing purposes
        cleared_sentence = self._data.replace(",", "")

        # set sentence and sentence_doc in corrector
        self.corrector.sentence = cleared_sentence
        self.corrector.sentence_doc = self.corrector.create_doc(
            cleared_sentence)

        # correct sentence and get result
        result: str = self.corrector.correct()

        # return rated result in format {'correct': int, 'incorrect': int, 'missing': int}
        return self._rate(result)
