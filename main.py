def main():
    filename = "books/frankenstein.txt"
    file_contents = get_file_contents(filename)
    word_count = count_words(file_contents)
    char_counts = count_chars(file_contents)
    print_report(filename, word_count, char_counts)


def print_report(filename, word_count, char_counts):
    char_counts_sorted = sort_counts(char_counts)
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    print()
    for count in char_counts_sorted:
        print(f"The '{count["char"]}' character was found {count["num"]} times")
    print(f"--- End report ---")


def sort_counts(char_counts):
    counts_list = [{"char": k, "num": v} for k, v in char_counts.items() if k.isalpha()]
    counts_list.sort(reverse=True, key=sort_on)
    return counts_list


def sort_on(dict):
    return dict["num"]


def get_file_contents(filename):
    with open(filename) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_chars(text):
    chars_seen = {}

    for char in text.lower():
        if char in chars_seen:
            chars_seen[char] += 1
        else:
            chars_seen[char] = 1

    return chars_seen


main()
