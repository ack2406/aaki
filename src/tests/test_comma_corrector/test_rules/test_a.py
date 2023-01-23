from ..test_comma_corrector import TestCommaCorrector


class TestA(TestCommaCorrector):
    def test_a(self):
        sentences = [
            "Zdecydowaliśmy się kupić mieszkanie, a nie dom."
        ]

        self.assertSentences(sentences)

    def test_a_także(self):
        sentences = [
            "Odpowiedzialność za to spoczywa na uczniach, a także ich rodzicach."
        ]

        self.assertSentences(sentences)