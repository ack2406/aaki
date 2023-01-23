from ..test_comma_corrector import TestCommaCorrector


class TestKiedy(TestCommaCorrector):
    def test_kiedy(self):
        sentences = [
            "Nie wiem, kiedy to się stało."
        ]

        self.assertSentences(sentences)

    def test_kiedy_pocz(self):
        sentences = [
            "Kiedy wracałam do domu, spadł deszcz."
        ]

        self.assertSentences(sentences)
    
    def test_kiedy_wtr(self):
        sentences = [
            "We wtorek, kiedy szłam do pracy, spotkałam Marka."
        ]

        self.assertSentences(sentences)