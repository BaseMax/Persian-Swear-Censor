def load_and_sort_words(file_path):
    """Load words from a file and sort them by length (longest to shortest)."""
    with open(file_path, "r", encoding="utf-8") as f:
        words = f.read().splitlines()

    return sorted(words, key=len, reverse=True)

def censor_text(input_text):
    """Replace offensive words in the input text with asterisks."""
    file_path = "words.txt"
    sorted_words = load_and_sort_words(file_path)

    with open(file_path, "w", encoding="utf-8") as f:
        for word in sorted_words:
            f.write(word + "\n")

    for word in sorted_words:
        censored_word = '*' * len(word)
        input_text = input_text.replace(word, censored_word)

    return input_text
