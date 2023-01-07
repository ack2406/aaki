from comma_corrector.comma_tester import CommaTester

def main():
    """Main function."""
    
    tester: CommaTester = CommaTester()
    tester.data = "To jest zdanie, które ma być poprawione."
    result = tester.test()

    print(result)


if __name__ == "__main__":
    main()