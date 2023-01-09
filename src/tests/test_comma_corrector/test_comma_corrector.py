import unittest

from aaki.comma_corrector.comma_corrector import CommaCorrector

class TestCommaCorrector(unittest.TestCase):
    def setUp(self) -> None:
        self.corrector = CommaCorrector()

    def test_aby(self) -> None:
        sentence = "Poszedł do sklepu aby kupić słodycze."
        no_commas_sentence = sentence.replace(",", "")

        self.corrector.sentences = [no_commas_sentence]
        self.assertEqual(self.corrector.run(), [sentence])
    
    def test_czy(self) -> None:
        sentence = "Tak naprawdę nie wiadomo, czy była tam tego dnia."
        no_commas_sentence = sentence.replace(",", "")

        self.corrector.sentences = [no_commas_sentence]
        self.assertEqual(self.corrector.run(), [sentence])
    
    def test_lub(self) -> None:
        sentence = "utro Adam pojedzie na zakupy lub umyje samochód."
        no_commas_sentence = sentence.replace(",", "")

        self.corrector.sentences = [no_commas_sentence]
        self.assertEqual(self.corrector.run(), [sentence])


if __name__ == '__main__':
    unittest.main()
