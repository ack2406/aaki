from ..test_comma_corrector import TestCommaCorrector


class TestJednak(TestCommaCorrector):
    def test_jednak_conj(self):
        sentences = [
            "Na miejsce przyjechała karetka pogotowia, jednak było już za późno."
        ]

        self.assertSentences(sentences)
    
    def test_jednak_pocz(self):
        sentences = [
            "Było bardzo zimno, postanowiliśmy jednak iść na spacer."
        ]

        self.assertSentences(sentences)

    def test_jednak_part(self):
        sentences = [
            "Miałeś jednak rację."
        ]

        self.assertSentences(sentences)
