from ..test_comma_corrector import TestCommaCorrector


class TestJako(TestCommaCorrector):
    def test_jako(self):
        sentences = [
            "Pojechał tam jako przedstawiciel naszego kraju."
        ]

        self.assertSentences(sentences)

    def test_jako_wtr(self):
        sentences = [
            "Szkoła, jako placówka oświatowa, powinna znać edukacyjne potrzeby uczniów."
        ]

        self.assertSentences(sentences)

    def test_jako_przycz(self):
        sentences = [
            "Był ceniony, jako wybitny naukowiec."
        ]

        self.assertSentences(sentences)

    def test_jako_że(self):
        sentences = [
            "Zadzwonił do niej, jako że nie przyszła dziś do szkoły."
        ]

        self.assertSentences(sentences)
    
    def test_jako_że_pocz(self):
        sentences = [
            "Jako że od miesiąca stosuję dietę, schudłam już pięć kilogramów."
        ]

        self.assertSentences(sentences)
    
    def test_jako_że_wtr(self):
        sentences = [
            "Moja mama, jako że jest pielęgniarką, mogła zrobić mi ten zastrzyk."
        ]

        self.assertSentences(sentences)