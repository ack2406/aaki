from ..test_comma_corrector import TestCommaCorrector


class TestJakby(TestCommaCorrector):
    def test_jakby(self):
        sentences = [
            "Przyjechałby do ciebie, jakby miał na to czas."
        ]

        self.assertSentences(sentences)

    def test_jakby_pocz(self):
        sentences = [
            "Jakby mógł, na pewno by to zrobił."
        ]

        self.assertSentences(sentences)

    def test_jakby_wtr(self):
        sentences = [
            "Nagle usłyszał coś, jakby grzmot, co przerwało panującą wokół ciszę."
        ]

        self.assertSentences(sentences)

    def test_jakby_wpro(self):
        sentences = [
            "Usłyszał jakby grzmot."
        ]

        self.assertSentences(sentences)
