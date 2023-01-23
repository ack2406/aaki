from ..test_comma_corrector import TestCommaCorrector


class TestAby(TestCommaCorrector):
    def test_aby_conj(self):
        sentences = [
            "Nastawiła budzik, aby wstać wcześnie."
        ]

        self.assertSentences(sentences)

    def test_tak_aby(self):
        sentences = [
            "Jechał szybko, tak aby zdążyli na samolot."
        ]

        self.assertSentences(sentences)

    def test_aby_part(self):
        sentences = [
            "Czy to aby działa?"
        ]

        self.assertSentences(sentences)
