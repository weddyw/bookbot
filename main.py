def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    wordcount(file_contents)
    char_count(file_contents)
    print("--- End report ---")


def wordcount(file_contents):
    words = file_contents.split()
    count = len(words)
    print(f"{count} words found in the document")


def char_count(file_contents):
    book = {}
    lowered_string = file_contents.lower()
    for char in lowered_string:
        if char.isalpha():
            if char in book:
                book[char] += 1
            else:
                book[char] = 1
    char_list = []
    for char, count in book.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")


def sort_on(dict):
    return dict["count"]


if __name__ == "__main__":
    main()
