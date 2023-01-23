from ..test_comma_corrector import TestCommaCorrector


class TestCzy(TestCommaCorrector):
    def test_czy_conj(self):
        sentences = [
            "Zjesz cukierka czy ciastko?"
        ]

        self.assertSentences(sentences)

    def test_czy_part(self):
        sentences = [
            "Nie wiem, czy to zrobił."
        ]

        self.assertSentences(sentences)
