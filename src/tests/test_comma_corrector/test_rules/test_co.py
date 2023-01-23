from ..test_comma_corrector import TestCommaCorrector


class TestCo(TestCommaCorrector):
    def test_co_wpro(self):
        sentences = [
            "Zapomniałam, co mówiłeś wczoraj."
        ]

        self.assertSentences(sentences)
    
    def test_co_przed_orz(self):
        sentences = [
            "To, co jest dobre dla ciebie, nie musi być odpowiednie dla mnie."
        ]

        self.assertSentences(sentences)
    
    def test_co_okol(self):
        sentences = [
            "Nie mam co robić."
        ]

        self.assertSentences(sentences)
    
    def test_co_part(self):
        sentences = [
            "Opuszczał lekcje co najmniej raz w tygodniu."
        ]

        self.assertSentences(sentences)