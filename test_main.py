import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


class CommandLineTests(unittest.TestCase):
    def test_utf8_russian_text(self):
        with TemporaryDirectory() as directory:
            book = Path(directory) / "book.txt"
            book.write_text("Привет мир", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "main.py", str(book)],
                capture_output=True,
                text=True,
                encoding="utf-8",
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Found 2 total words", result.stdout)
        self.assertIn("р: 2", result.stdout)

    def test_invalid_utf8_reports_an_error(self):
        with TemporaryDirectory() as directory:
            book = Path(directory) / "book.txt"
            book.write_bytes(b"\xff\xfe")
            result = subprocess.run(
                [sys.executable, "main.py", str(book)],
                capture_output=True,
                text=True,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("file is not valid UTF-8", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_missing_book_reports_an_error(self):
        with TemporaryDirectory() as directory:
            missing_book = Path(directory) / "missing.txt"
            result = subprocess.run(
                [sys.executable, "main.py", str(missing_book)],
                capture_output=True,
                text=True,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Could not read book", result.stderr)
        self.assertIn(str(missing_book), result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
