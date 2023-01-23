from ..test_comma_corrector import TestCommaCorrector


class TestChoć(TestCommaCorrector):
    def test_choć_conj(self):
        sentences = [
            "Uprawiał sport, choć był niepełnosprawny."
        ]

        self.assertSentences(sentences)
    
    def test_choć_conj_pocz(self):
        sentences = [
            "Choć jestem przeziębiony, muszę iść do pracy."
        ]

        self.assertSentences(sentences)
    
    def test_choć_part(self):
        sentences = [
            "Zrób choć zakupy."
        ]

        self.assertSentences(sentences)