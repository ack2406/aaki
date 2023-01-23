from ..test_comma_corrector import TestCommaCorrector


class TestAlbo(TestCommaCorrector):
    def test_albo_powt(self):
        sentences = [
            "Albo pójdziemy do teatru, albo do kina."
        ]

        self.assertSentences(sentences)
    
    def test_albo_dopow(self):
        sentences = [
            "Był zawsze uczniem niezwykle zdolnym, albo raczej bardzo pilnym."
        ]

        self.assertSentences(sentences)
    

    def test_albo_wtr(self):
        sentences = [
            "Zwykle jestem bardzo ostrożna, albo raczej tchórzliwa, dlatego unikam niepewnych sytuacji."
        ]

        self.assertSentences(sentences)
    
    def test_albo_rown(self):
        sentences = [
            "Teraz albo nigdy."
        ]

        self.assertSentences(sentences)
