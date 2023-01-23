from ..test_comma_corrector import TestCommaCorrector


class TestAni(TestCommaCorrector):
    def test_ani(self):
        sentences = [
            "Nie chcę herbaty ani kawy."
        ]

        self.assertSentences(sentences)

    def test_ani_wtr(self):
        sentences = [
            "Nie przyszedł na umówione spotkanie, ani też nie zawiadomił nikogo.",
        ]

        self.assertSentences(sentences)

    def test_ani_powt(self):
        sentences = [
            "Nie mogłam ruszyć ani ręką, ani nogą."
        ]

        self.assertSentences(sentences)

    def test_ani_part(self):
        sentences = [
            "Nie miał ani grosza."
        ]

        self.assertSentences(sentences)