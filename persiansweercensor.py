import os

def load_and_sort_words(file_path):
    """Load words from a file, trim them, and sort them by length (longest to shortest)."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
    except IOError as e:
        raise IOError(f"An error occurred while reading the file {file_path}: {e}")

    return sorted(words, key=len, reverse=True)

def censor_text(input_text):
    """Replace offensive words in the input text with asterisks."""
    file_path = "words/persian.txt"
    try:
        sorted_words = load_and_sort_words(file_path)
    except (FileNotFoundError, IOError) as e:
        print(e)
        return input_text

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for word in sorted_words:
                f.write(word + "\n")
    except IOError as e:
        print(f"An error occurred while writing to the file {file_path}: {e}")
        return input_text

    for word in sorted_words:
        censored_word = '*' * len(word)
        input_text = input_text.replace(word, censored_word)

    return input_text

