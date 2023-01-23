from ..test_comma_corrector import TestCommaCorrector


class TestNatomiast(TestCommaCorrector):
    def test_natomiast(self):
        sentences = [
            "Nie mam ochoty na lody, natomiast z przyjemnością zjem kawałek tortu."
        ]

        self.assertSentences(sentences)
    
    def test_natomiast_poprz(self):
        sentences = [
            "My natomiast musimy ustalić plan działania."
        ]

        self.assertSentences(sentences)