from ..test_comma_corrector import TestCommaCorrector


class TestNiż(TestCommaCorrector):
    def test_niż_podrz(self):
        sentences = [
            "Jest gorzej, niż sądziłem."
        ]

        self.assertSentences(sentences)

    def test_niż_bezok(self):
        sentences = [
            "Wolę poczekać, niż stracić tę szansę."
        ]

        self.assertSentences(sentences)

    def test_niż_porown(self):
        sentences = [
            "Małgosia jest ładniejsza niż jej siostra."
        ]

        self.assertSentences(sentences)
