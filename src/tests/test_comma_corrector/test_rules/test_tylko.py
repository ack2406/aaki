from ..test_comma_corrector import TestCommaCorrector


class TestTylko(TestCommaCorrector):
    def test_tylko(self):
        sentences = [
            "Nic nie mówił, tylko spojrzał na mnie."
        ]

        self.assertSentences(sentences)

    def test_tylko_part(self):
        sentences = [
            "Kupiłam tylko masło i mąkę."
        ]

        self.assertSentences(sentences)
    
    def test_tylko_że(self):
        sentences = [
            "Ta książka jest bardzo ciekawa, tylko że za długa."
        ]

        self.assertSentences(sentences)