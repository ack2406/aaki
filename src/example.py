from aaki import CommaCorrector


corrector = CommaCorrector()

sentences = [
    "Ile dałbym by zapomnieć Cię.",
    "Wszystkie chwile te które są na nie."
    ]

corrected_sentences = corrector.correct(sentences)

print(corrected_sentences)