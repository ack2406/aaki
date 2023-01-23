from ..test_comma_corrector import TestCommaCorrector


class TestŻe(TestCommaCorrector):
    def test_że(self):
        sentences = [
            "Powiedziała, że chce jak najszybciej skończyć pracę."
        ]

        self.assertSentences(sentences)

    def test_chyba_że(self):
        sentences = [
            "Nie zrobię tego, chyba że coś mi obiecasz."
        ]

        self.assertSentences(sentences)

    def test_mimo_że(self):
        sentences = [
            "Nie byłam głodna, mimo że nic dziś nie jadłam."
        ]

        self.assertSentences(sentences)

    def test_mimoże_pocz(self):
        sentences = [
            "Mimo że dbam o swoje zdrowie, ciągle źle się czuję."
        ]

        self.assertSentences(sentences)

    def test_mimo_że_wtr(self):
        sentences = [
            "Znów, mimo że dużo się uczyłam, nie zdałam egzaminu."
        ]

        self.assertSentences(sentences)

    def test_z_tym_że(self):
        sentences = [
            "Zacznę dziś czytać tę książkę, z tym że dopiero wieczorem."
        ]

        self.assertSentences(sentences)