from ..test_comma_corrector import TestCommaCorrector


class TestJeśli(TestCommaCorrector):
    def test_jeśli(self):
        sentences = [
            "Zadzwonię do ciebie, jeśli tylko będę mogła."
        ]

        self.assertSentences(sentences)
    
    def test_jeśli_pocz(self):
        sentences = [
            "Jeśli się nie myślę, jutro masz urodziny."
        ]

        self.assertSentences(sentences)