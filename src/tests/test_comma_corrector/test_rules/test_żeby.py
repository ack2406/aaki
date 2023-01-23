from ..test_comma_corrector import TestCommaCorrector


class TestŻeby(TestCommaCorrector):
    def test_żeby(self):
        sentences = [
            "Muszę dużo się uczyć, żeby zdać egzaminy."
        ]

        self.assertSentences(sentences)
    
    def test_żeby_pocz(self):
        sentences = [
            "Żeby odpocząć, muszę wyjechać."
        ]

        self.assertSentences(sentences)
