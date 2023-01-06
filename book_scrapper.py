import requests
import re
import string

BOOKS = [
    'gliscinski-dyskursy-prawa-autorskiego',
    'wyka-modernizm-polski',
    'wyka-rzecz-wyobrazni',
    'kijowski-dziecko-przez-ptaka-przyniesione'
]


def get_book_txt(book_url):
    """Return book text from given url."""

    url = f"https://wolnelektury.pl/media/book/txt/{book_url}.txt"
    response = requests.get(url)
    return response.text


def save_to_txt_file(file_name, file_content):
    """Save given content to txt file."""

    with open(f"resources/{file_name}.txt", 'w+', encoding="utf-8") as file:
        # write every element in list in new line
        for element in file_content:
            file.write(element + '\n')


def format_book(book_url):
    """Return formatted book text."""

    book = get_book_txt(book_url)
    book = re.split(r'\n|–|—|…|\xa0', book)

    # split elements by ., !, ? but keep the separators
    book = [re.split(r'(?<=[.!?]) +', x) for x in book]

    # flatten the list of lists
    book = [item for sublist in book for item in sublist]

    # remove all elements that are shorter than 8 words
    book = list(filter(lambda x: len(x.split()) > 8, book))

    # # remove white spaces
    book = [x.strip() for x in book]

    # remove all elements that have a letter at the end
    book = list(
        filter(lambda x: not x[-1].isalpha(), book))

    # remove all elements that starts with small letter
    book = list(filter(lambda x: not x[0].islower(), book))

    # remove all elements that has : or „
    book = list(
        filter(lambda x: not ':' in x and not '„' in x, book))

    # remove all elements that has punctuation characters aside from ., !, ?
    book = [x for x in book if all(ch not in x for ch in string.punctuation.replace('?', '').replace(
        '!', '').replace('.', '').replace(',', '') + '\xa0\n')]

    # remove redundant spaces
    book = [re.sub(r'\s+', ' ', x) for x in book]

    # remove all elements that doesn't have a dot, exclamation mark or question mark at the end
    book = list(filter(lambda x: x[-1] in '.?!', book))

    return book


def main():
    """Main function."""
    
    for book_url in BOOKS:
        book = format_book(book_url)
        save_to_txt_file(book_url, book)


if __name__ == '__main__':
    main()
