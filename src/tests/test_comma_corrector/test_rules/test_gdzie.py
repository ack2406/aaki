from ..test_comma_corrector import TestCommaCorrector


class TestGdzie(TestCommaCorrector):
    def test_gdzie(self):
        sentences = [
            "Wiem, gdzie jesteś."
        ]

        self.assertSentences(sentences)
    
    def test_gdzie_pocz(self):
        sentences = [
            "Gdzie dwóch się bije, tam trzeci korzysta."
        ]

        self.assertSentences(sentences)
    
    def test_gdzie_wtr(self):
        sentences = [
            "Tam, gdzie się znalazł, było pusto i cicho."
        ]

        self.assertSentences(sentences)
    
    def test_gdzie_join(self):
        sentences = [
            "Pojechał na wieś, tam gdzie się urodził."
        ]

        self.assertSentences(sentences)