from ..test_comma_corrector import TestCommaCorrector


class TestAle(TestCommaCorrector):
    def test_ale_conj(self):
        sentences = [
            "Zrobiła to, ale niedokładnie."
        ]

        self.assertSentences(sentences)

    def test_ale_part(self):
        sentences = [
            "Zobacz, ale samochód!"
        ]

        self.assertSentences(sentences)

    def test_ale_excl(self):
        sentences = [
            "Ale, ale, czy już jej powiedziałeś?"
        ]

        self.assertSentences(sentences)

    def test_ale_noun(self):
        sentences = [
            "Ona zwykle ma jakieś ale."
        ]

        self.assertSentences(sentences)
