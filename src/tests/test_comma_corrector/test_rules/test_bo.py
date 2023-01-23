from ..test_comma_corrector import TestCommaCorrector


class TestBo(TestCommaCorrector):
    def test_bo(self):
        sentences = [
            "Zostaniemy dziś w domu, bo na dworze jest bardzo zimno."
        ]

        self.assertSentences(sentences)