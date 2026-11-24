## bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot analyzes a text file and reports its word count and the frequency of each letter.

## Usage

Requires Python 3.12 or later. From the project directory, run:

```sh
python3 main.py path/to/book.txt
```

The book must be a UTF-8 encoded text file. The report lists the total number of words followed by letters in descending order of frequency. If the file cannot be read, BookBot prints an error message and exits with a nonzero status.
