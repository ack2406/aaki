from ..test_comma_corrector import TestCommaCorrector


class TestWraz(TestCommaCorrector):
    def test_wraz(self):
        sentences = [
            "Wybraliśmy się wraz z Markiem do kina."
        ]

        self.assertSentences(sentences)
    
    def test_wraz_wtr(self):
        sentences = [
            "Ta sytuacja staje się dziś, wraz z towarzyszącymi jej okolicznościami, niezwykle trudna."
        ]

        self.assertSentences(sentences)