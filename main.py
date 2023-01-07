from comma_corrector.multi_comma_corrector import MultiCommaCorrector
from comma_corrector.comma_tester import CommaTester

def main():
    """Main function."""
    

    corrector = MultiCommaCorrector()

    # daj mi polskie zdania
    sentences = [
        "To jest zdanie bez przecinka ale za to z głową.",
        "Muchy, biedronki oraz owady nie są zwierzętami ale są roślinami.",
        "Patryk poszedł do sklepu i spotkał się z kolegą, który mówił, że nie ma pieniędzy.",
        "Patryk ma dobre serce, lecz nie jest szczęśliwy.",
        "Patryk powiedział że nie ma pieniędzy, a jego kolega się zdenerwował",
        "Patryk i kolega chcieli walczyć o pieniądze lecz policjant ich rozproszył.",
        "Kolega Patryka gonił go, ponieważ Patryk nie chciał mu oddać pieniędzy.",
        "Nikt już nie chce Patryka ponieważ on jest zły.",
    ]

    corrector.sentences = sentences
    corrector.sentences_doc = corrector.create_docs(corrector.sentences)

    corrected_sentences = corrector.correct()

    for sentence in corrected_sentences:
        print(sentence)





if __name__ == "__main__":
    main()