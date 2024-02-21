def get_book(path):
    with open(path) as f:
        return f.read()

def word_count(string_to_parse):
    words_list = string_to_parse.split()
    return len(words_list)

def char_count(string_to_parse):
    count_of_chars = {}
    words_list = string_to_parse.split()
    for word in words_list:
        for letter in word:
            lower_case_letter = letter.lower()

            if lower_case_letter not in count_of_chars:
                count_of_chars[lower_case_letter] = 1

            count_of_chars[lower_case_letter] += 1

    return count_of_chars

def final_report(body_of_text):
    final_report_list = []

    for key, value in body_of_text.items():
        if key.isalpha():
            final_report_list.append({"Letter": key, "total": value})

    def sort_on(dict):
        return dict["total"]

    final_report_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(get_book("./books/Frankenstein book.txt"))} words found in the document\n\n")

    for line in final_report_list:
        print(f"The '{line["Letter"] }' character was found {line["total"]} times")
    print("--- End report ---")








def main():
    final_report(char_count(get_book("./books/Frankenstein book.txt")))

if __name__ == '__main__':
    main()
