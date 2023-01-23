from ..test_comma_corrector import TestCommaCorrector


class TestI(TestCommaCorrector):
    def test_i_conj(self):
        sentences = [
            "Dostałam od niego książkę i kwiaty."
        ]

        self.assertSentences(sentences)

    def test_i_wspl(self):
        sentences = [
            "Lubię słuchać muzyki i czytać książki."
        ]

        self.assertSentences(sentences)

    def test_i_powt(self):
        sentences = [
            "Lubię jabłka i gruszki, i jeszcze śliwki."
        ]

        self.assertSentences(sentences)

    def test_i_powt_not_rown(self):
        sentences = [
            "Byłem w kinie i spotkałem tam Piotrka i Marcina."
        ]

        self.assertSentences(sentences)

    def test_i_wtr(self):
        sentences = [
            "Znam ją od dawna, i to bardzo dobrze."
        ]

        self.assertSentences(sentences)

    def test_i_zam_podrz(self):
        sentences = [
            "Lubię oglądać filmy, które trzymają w napięciu, i słuchać muzyki, która mnie relaksuje."
        ]

        self.assertSentences(sentences)

    def test_i_cons_conj(self):
        sentences = [
            "Nie spałem dziś w nocy, i jestem bardzo zmęczony."
        ]

        self.assertSentences(sentences)
