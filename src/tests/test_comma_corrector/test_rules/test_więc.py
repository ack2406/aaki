from ..test_comma_corrector import TestCommaCorrector


class TestWięc(TestCommaCorrector):
    def test_więc_cons_conj(self):
        sentences = [
            "Cały dzień pracowałem, więc teraz jestem zmęczony."
        ]

        self.assertSentences(sentences)
    
    def test_więc_enum(self):
        sentences = [
            "Na miejscu stawili się wszyscy, a więc dyrektor, nauczyciele i uczniowie."
        ]

        self.assertSentences(sentences)
    
    def test_więc_part(self):
        sentences = [
            "Do widzenia więc!"
        ]

        self.assertSentences(sentences)