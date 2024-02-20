def get_book(path):
    with open(path) as f:
        return f.read()

def word_count(string_to_parse):
    words_list = string_to_parse.split()
    return len(words_list)



def main():
    print(word_count(get_book("./books/Frankenstein book.txt")))

if __name__ == '__main__':
    main()
