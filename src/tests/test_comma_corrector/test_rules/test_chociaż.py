from ..test_comma_corrector import TestCommaCorrector


class TestChociaż(TestCommaCorrector):
    def test_chociaż(self):
        sentences = [
            "Zdał egzamin, chociaż w ogóle się nie uczył."
        ]

        self.assertSentences(sentences)
    
    def test_chociaż_pocz(self):
        sentences = [
            "Chociaż jestem chory, pójdę dziś do pracy."
        ]

        self.assertSentences(sentences)
    
    def test_chociaż_part(self):
        sentences = [
            "Mogłaś chociaż przeprosić."
        ]

        self.assertSentences(sentences)