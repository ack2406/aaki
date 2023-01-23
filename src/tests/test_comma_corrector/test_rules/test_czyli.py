from ..test_comma_corrector import TestCommaCorrector


class TestCzyli(TestCommaCorrector):
    def test_czyli(self):
        sentences = [
            "Przyjdę do ciebie po lekcjach, czyli około piętnastej."
            ]

        self.assertSentences(sentences)
    
    def test_czyli_wtr(self):
        sentences = [
            "Wiek pary i elektryczności, czyli wiek XIX, oznaczał wielką rewolucję przemysłową."
        ]

        self.assertSentences(sentences)