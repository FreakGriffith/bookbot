from stats import get_book_text, count_symbols, sort_symbols, count_words
import sys

def main():
    path = ""
    
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_text(path)
    words = count_words(book)
    list_of_symbols = count_symbols(book)
    sorted_list_of_symbols = sort_symbols(list_of_symbols)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for i in sorted_list_of_symbols:
        print(i["name"] + ":", i["num"])
    print("============= END ===============")
    

main()