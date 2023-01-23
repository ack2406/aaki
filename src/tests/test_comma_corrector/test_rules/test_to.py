from ..test_comma_corrector import TestCommaCorrector


class TestTo(TestCommaCorrector):
    def test_to(self):
        sentences = [
            "Chcesz, to idź tam."
        ]

        self.assertSentences(sentences)

    def test_to_compl(self):
        sentences = [
            "Jeśli chcesz, to zostań tutaj."
        ]

        self.assertSentences(sentences)

    def test_to_join(self):
        sentences = [
            "Do ciasta dodaj przyprawy korzenne, to jest cynamon, goździki, kardamon i anyż."
        ]

        self.assertSentences(sentences)

    def test_to_conn(self):
        sentences = [
            "Zakopane to zimowa stolica Polski."
        ]

        self.assertSentences(sentences)