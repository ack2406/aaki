from ..test_comma_corrector import TestCommaCorrector


class TestSkoro(TestCommaCorrector):
    def test_skoro(self):
        sentences = [
            "Zrobię to, skoro tak nalegasz."
        ]

        self.assertSentences(sentences)

    def test_skoro_pocz(self):
        sentences = [
            "Skoro nie możesz mi pomóc, to chociaż nie przeszkadzaj."
        ]

        self.assertSentences(sentences)

    def test_skoro_wtr(self):
        sentences = [
            "Postanowiłam, że pod koniec wakacji, skoro wtedy mam urlop, wybiorę się do Paryża."
        ]

        self.assertSentences(sentences)
