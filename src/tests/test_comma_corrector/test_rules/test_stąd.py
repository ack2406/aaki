from ..test_comma_corrector import TestCommaCorrector


class TestStąd(TestCommaCorrector):
    def test_stąd_conj(self):
        sentences = [
            "Często opuszczał lekcje, stąd miał duże kłopoty w nauce."
        ]

        self.assertSentences(sentences)

    def test_stąd_poj(self):
        sentences = [
            "Jak się stąd wyrwać?"
        ]

        self.assertSentences(sentences)
    
    def test_stąd_od_tego(self):
        sentences = [
            "Zaczął opuszczać lekcje, stąd już tylko krok do kłopotów w nauce."
        ]

        self.assertSentences(sentences)