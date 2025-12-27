

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def count_words(text):
    words = text.split()
    return len(words)

def count_symbols(text):
    text = text.lower()
    list_of_unique_symbols = []
    symbols = {}

    for i in text:
        list_of_unique_symbols.append(i)
    
    set_of_unique_symbols = set(list_of_unique_symbols)
    
    for i in set_of_unique_symbols:
        if i.isalpha():
            symbols[i] = 0

    for i in range(len(text)):
        char = text[i]
        if char in symbols:
            symbols[char] += 1
    
    return symbols

def help_sorf_function(items):
    return items["num"]

def sort_symbols(list_of_symbols):
    list_of_dicts = []

    for i in list_of_symbols:
        if i.isalpha():
            count = 0
            for j in list_of_symbols:
                if i == j:
                    count = list_of_symbols[j]

            new_dict = {"name" : i , "num": count}

            list_of_dicts.append(new_dict)
        
    list_of_dicts.sort(key=help_sorf_function, reverse=True)
    return list_of_dicts

