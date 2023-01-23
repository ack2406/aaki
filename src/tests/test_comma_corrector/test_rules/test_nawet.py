from ..test_comma_corrector import TestCommaCorrector


class TestNawet(TestCommaCorrector):
    def test_nawet(self):
        sentences = [
            "Przyszła i nawet się nie odezwała."
        ]

        self.assertSentences(sentences)

    def test_nawet_konkr(self):
        sentences = [
            "U nas jest zimno, nawet latem."
        ]

        self.assertSentences(sentences)

    def test_nawet_srod(self):
        sentences = [
            "Jego książki były dobre, nawet świetne, ale nie zgodził się na ich publikację."
        ]

        self.assertSentences(sentences)