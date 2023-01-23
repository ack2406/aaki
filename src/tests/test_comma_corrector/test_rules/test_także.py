from ..test_comma_corrector import TestCommaCorrector


class TestTakże(TestCommaCorrector):
    def test_także(self):
        sentences = [
            "Ona także się boi."
        ]

        self.assertSentences(sentences)

    def test_także_dop(self):
        sentences = [
            "Nie tylko nauczyciele, także uczniowie mają swoje prawa i obowiązki."
        ]

        self.assertSentences(sentences)
