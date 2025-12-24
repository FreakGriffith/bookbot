def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)

main()