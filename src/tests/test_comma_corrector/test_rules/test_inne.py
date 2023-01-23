from ..test_comma_corrector import TestCommaCorrector


class TestInne(TestCommaCorrector):
    def test_poza_tym(self):
        sentences = [
            "Ugotowałam obiad, poza tym zrobiłam deser."
        ]

        self.assertSentences(sentences)

    def test_dzięki_temu(self):
        sentences = [
            "Na dworzec dotarłem o szesnastej, dzięki temu zdążyłem na pociąg."
        ]

        self.assertSentences(sentences)
    
    def test_dzięki_temu_rzecz_cel(self):
        sentences = [
            "Zdałam ten egzamin dzięki twojej pomocy."
        ]

        self.assertSentences(sentences)
    
    def test_dzięki_temu_pocz(self):
        sentences = [
            "Dzięki temu nauczycielowi polubiłam fizykę."
        ]

        self.assertSentences(sentences)
    
    def test_co_więcej(self):
        sentences = [
            "Nie sądziłam, że mnie to spotka, co więcej, myślałam, że to wręcz nierealne."
        ]

        self.assertSentences(sentences)