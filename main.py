from comma_corrector.multi_comma_corrector import MultiCommaCorrector
from comma_corrector.comma_tester import CommaTester
from comma_corrector.multi_comma_tester import MultiCommaTester


def main():
    """Main function."""

    tester = MultiCommaTester()

    # get sentences from file resources/wyka-rzecz-wyobrazni.txt
    with open("resources/wyka-rzecz-wyobrazni.txt", "r", encoding="utf-8") as file:
        sentences = file.readlines()
    

    tester.data = sentences

    points = tester.test()

    print(points)


if __name__ == "__main__":
    main()
