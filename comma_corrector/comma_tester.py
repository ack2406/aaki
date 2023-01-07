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
        data_doc: Language = self.corrector.create_doc(self._data)
        corrected_doc: Language = self.corrector.create_doc(corrected_sentence)


        data_pos: int = 0
        corrected_pos: int = 0

        points: dir[str, int] = {"correct": 0, "incorrect": 0, "missing": 0}

        while data_pos < len(data_doc) and corrected_pos < len(corrected_doc):
            data_token: tokens.token.Token = data_doc[data_pos]
            corrected_token: tokens.token.Token = corrected_doc[corrected_pos]

            if data_token.text == ',' and corrected_token.text == ',':
                points["correct"] += 1
            elif data_token.text == ',' and corrected_token.text != ',':
                points["missing"] += 1
                corrected_pos -= 1
            elif data_token.text != ',' and corrected_token.text == ',':
                points["incorrect"] += 1
                data_pos -= 1

            data_pos += 1
            corrected_pos += 1
        
        return points

    def test(self) -> dict[str, int]:
        cleared_sentence = self._data.replace(",", "")
        self.corrector.sentence = cleared_sentence
        result: str = self.corrector.correct()

        return self._rate(result)
