from ..test_comma_corrector import TestCommaCorrector


class TestJak(TestCommaCorrector):
    def test_jak(self):
        sentences = [
            "Adam był tak samo szybki jak Dawid."
        ]

        self.assertSentences(sentences)

    def test_podobnie_jak(self):
        sentences = [
            "Ona ubrała się podobnie jak ja."
        ]

        self.assertSentences(sentences)

    def test_podobnie_jak_wtr(self):
        sentences = [
            "Dzisiaj i wczoraj, podobnie jak dwa dni temu, padał deszcz."
        ]

        self.assertSentences(sentences)
    
    def test_jak_również(self):
        sentences = [
            "Lubię filmy przygodowe, obyczajowe, jak również sensacyjne."
        ]

        self.assertSentences(sentences)
    
    def test_taki_jak(self):
        sentences = [
            "Człowiek taki jak ty nie powinien zabierać głosu w tej sprawie."
        ]

        self.assertSentences(sentences)
    
    def test_jak_i(self):
        sentences = [
            "Martwił mnie jej stan zdrowia, jak i to, że nie wiedziałem, co nastąpi potem."
        ]

        self.assertSentences(sentences)