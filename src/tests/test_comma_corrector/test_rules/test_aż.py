from ..test_comma_corrector import TestCommaCorrector


class TestAż(TestCommaCorrector):
    def test_aż_conj(self):
        sentences = [
            "Długo milczał, aż nagle krzyknął."
        ]

        self.assertSentences(sentences)

    def test_aż_part(self):
        sentences = [
            "Zjadł aż pięć kawałków tortu."
        ]

        self.assertSentences(sentences)
