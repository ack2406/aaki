from ..test_comma_corrector import TestCommaCorrector


class TestPonieważ(TestCommaCorrector):
    def test_ponieważ(self):
        sentences = [
            "Nie mogę teraz rozmawiać, ponieważ jestem bardzo zajęty."
        ]
    
        self.assertSentences(sentences)
    
    def test_ponieważ_pocz(self):
        sentences = [
            "Ponieważ jestem bardzo zmęczona, muszę położyć się dziś wcześnie spać."
        ]
    
        self.assertSentences(sentences)
    
    def test_ponieważ_wtr(self):
        sentences = [
            "Dzisiejsze zebranie, ponieważ było bardzo ważne, przedłużyło się o godzinę."
        ]
    
        self.assertSentences(sentences)