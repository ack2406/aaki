from ..test_comma_corrector import TestCommaCorrector


class TestLub(TestCommaCorrector):
    def test_lub_conj(self):
        sentences = [
            "Jutro Adam pojedzie na zakupy lub umyje samochód."
        ]

        self.assertSentences(sentences)

    def test_lub_poj(self):
        sentences = [
            "Do cioci pojedziemy we wtorek lub w środę."
        ]

        self.assertSentences(sentences)

    def test_lub_powt(self):
        sentences = [
            "Jutro Adam pojedzie na zakupy lub umyje samochód, lub ugotuje obiad."
        ]

        self.assertSentences(sentences)

    def test_lub_dopow(self):
        sentences = [
            "Na obiad zjemy zupę, którą przywiezie ciocia, lub zamówimy coś z restauracji."
        ]

        self.assertSentences(sentences)
