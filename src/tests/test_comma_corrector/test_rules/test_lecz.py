from ..test_comma_corrector import TestCommaCorrector


class TestLecz(TestCommaCorrector):
    def test_lecz(self):
        sentences = [
            "Zawsze byłam optymistką, lecz ostatnio mam czarne myśli."
        ]

        self.assertSentences(sentences)