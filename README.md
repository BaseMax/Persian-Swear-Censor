# Persian Swear Censor

Persian Swear Censor is a Python script that censors offensive words in Persian text by replacing them with asterisks. The script reads a list of offensive words from a file, sorts them by length, and then replaces occurrences of these words in the input text.

## Features

- Load offensive words from a file
- Trim and sort words by length (longest to shortest)
- Replace offensive words in the input text with asterisks
- Handle file access errors gracefully

## Installation

1. Clone the repository:

```bash
git clone https://github.com/BaseMax/Persian-Swear-Censor.git
cd Persian-Swear-Censor
```

Ensure you have Python installed (version 3.6 or higher).

### Usage

1. Create a file named `words.txt` in the project directory and add the offensive words you want to censor, one per line.

2. Use the `censor_text` function in your Python script:

```python
from persiansweercensor import censor_text

input_text = "Your input text here"
censored_text = censor_text(input_text)
print(censored_text)
```

### Example

Given the following words.txt file:

```
badword1
badword2
```

And the following input text:

```
input_text = "This is a badword1 and another badword2."
```

The output will be:

```
This is a ******* and another *******.
```

### Error Handling

The script includes error handling to ensure that the file exists and is accessible. If the file is not found or cannot be read, an appropriate error message will be printed, and the original input text will be returned.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contact

For any questions or suggestions, feel free to open an issue or contact the repository owner.

Copyright 2024, Max Base
