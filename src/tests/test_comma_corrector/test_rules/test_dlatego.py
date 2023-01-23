from ..test_comma_corrector import TestCommaCorrector


class TestDlatego(TestCommaCorrector):
    def test_dlatego(self):
        sentences = [
            "Byłem zmęczony, dlatego zasnąłem bardzo wcześnie."
        ]

        self.assertSentences(sentences)
