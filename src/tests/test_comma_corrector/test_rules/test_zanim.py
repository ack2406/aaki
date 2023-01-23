from ..test_comma_corrector import TestCommaCorrector


class TestZanim(TestCommaCorrector):
    def test_zanim(self):
        sentences = [
            "Wyszłam, zanim wróciłeś do domu."
        ]

        self.assertSentences(sentences)

    def test_zanim_pocz(self):
        sentences = [
            "Zanim odpowiesz, zastanów się dobrze."
        ]

        self.assertSentences(sentences)

    def test_zanim_wtr(self):
        sentences = [
            "Zawsze, zanim wyjdę z domu, sprawdzam, czy zamknęłam wszystkie okna."
        ]

        self.assertSentences(sentences)