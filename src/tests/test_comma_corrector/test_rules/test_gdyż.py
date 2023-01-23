from ..test_comma_corrector import TestCommaCorrector


class TestGdyż(TestCommaCorrector):
    def test_gdyż(self):
        sentences = [
            "Nie mogę z tobą jechać, gdyż jestem chora."
        ]

        self.assertSentences(sentences)