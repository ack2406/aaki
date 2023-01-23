from ..test_comma_corrector import TestCommaCorrector


class TestKtóry(TestCommaCorrector):
    def test_który(self):
        sentences = [
            "Nie wiem, który z was mówi prawdę."
        ]

        self.assertSentences(sentences)

    def test_który_pocz(self):
        sentences = [
            "Który z nich jest godny zaufania, naprawdę nie wiem."
        ]

        self.assertSentences(sentences)

    def test_który_wtr(self):
        sentences = [
            "Obraz, który widzimy, pochodzi z XVIII wieku."
        ]

        self.assertSentences(sentences)

    def test_który_join(self):
        sentences = [
            "To jest dom, w którym się wychowałam."
        ]

        self.assertSentences(sentences)

    def test_który_powt(self):
        sentences = [
            "Znałam kobietę, która uwielbiała koty i która miała ich w domu aż osiem."
        ]

        self.assertSentences(sentences)
