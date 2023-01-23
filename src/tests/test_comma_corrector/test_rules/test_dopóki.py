from ..test_comma_corrector import TestCommaCorrector


class TestDopóki(TestCommaCorrector):
    def test_dopóki(self):
        sentences = [
            "Biegłem, dopóki nie poczułem zmęczenia."
        ]

        self.assertSentences(sentences)
    
    def test_dopóki_pocz(self):
        sentences = [
            "Dopóki trwały wakacje, byliśmy szczęśliwi."
        ]

        self.assertSentences(sentences)
    
    def test_dopóki_wtr(self):
        sentences = [
            "Tak długo, dopóki na morzu był sztorm, musieliśmy czekać cierpliwie w porcie."
        ]

        self.assertSentences(sentences)
    

    def test_dopóki_dopóty(self):
        sentences = [
            "Dopóki był upał, dopóty nie wychodziłem z domu."
        ]

        self.assertSentences(sentences)
