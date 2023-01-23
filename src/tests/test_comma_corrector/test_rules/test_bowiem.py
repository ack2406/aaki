from ..test_comma_corrector import TestCommaCorrector


class TestBowiem(TestCommaCorrector):
    def test_bowiem(self):
        sentences = [
            "Nie przyszedł dziś do szkoły, bowiem zachorował."
        ]

        self.assertSentences(sentences)

    def test_bowiem_srod(self):
        sentences = [
            "Nie zrobiłam zakupów, zapomniałam bowiem zabrać ze sobą portfel."
        ]

        self.assertSentences(sentences)

    def test_bowiem_poprz(self):
        sentences = [
            "Był on bowiem wielokrotnie poruszany w naszym gronie."
        ]

        self.assertSentences(sentences)
