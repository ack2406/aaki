from comma_corrector.comma_tester import CommaTester
from comma_corrector.comma_corrector import CommaCorrector


def main():
    """Main function."""

    # get sentences from file resources/wyka-rzecz-wyobrazni.txt
    with open("resources/wyka-rzecz-wyobrazni.txt", "r", encoding="utf-8") as file:
        sentences = [line.strip() for line in file.readlines()]

    corrector = CommaCorrector(sentences)
    tester = CommaTester(sentences)

    print(corrector.run()[:10])
    print(tester.run())


if __name__ == "__main__":
    main()
