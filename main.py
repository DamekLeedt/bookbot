def main():
    file_contents = get_book_text("books/frankenstein.txt")
    report(file_contents, "books/frankenstein.txt")

def count_words(s):
    # Big shock incoming: you could shorten this to len(s.split()) and get the same answer.
    # Fuck's going on.
    word_array = s.replace("\n", " ").split(' ')

    return len(word_array) - word_array.count("")

def count_letters(s):
    letter_amount = {}
    s = s.lower()
    for character in s:
        if character in letter_amount:
            letter_amount[character] += 1
        else:
            letter_amount[character] = 1
    return letter_amount

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(dict):
    return dict["num"]

def report(s, path):
    letters = count_letters(s)
    sorted_letters = []
    for key in letters:
        if key.isalpha():
            sorted_letters.append({"name": key, "num": letters[key]})
    sorted_letters.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(s)} words found in the document\n")
    for item in sorted_letters:
        print(f"The {item["name"]} was found {item["num"]} times")
    print("--- End report ---")

    return None

main()