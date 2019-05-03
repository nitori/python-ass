#!/usr/bin/env python

import ass
import unittest
from pathlib import Path

from io import StringIO

folder = Path(__file__).parent


class TestEverything(unittest.TestCase):

    test_ass = Path(folder, "test.ass")

    def test_parse_dump(self):
        with self.test_ass.open("r", encoding='utf_8_sig') as f:
            contents = f.read()

        doc = ass.parse(StringIO(contents))
        out = StringIO()
        doc.dump_file(out)

        assert out.getvalue().strip() == contents.strip()

    def test_parse_encoding(self):
        with self.test_ass.open("r", encoding='utf_8') as f:
            with self.assertRaises(ValueError):
                ass.parse(f)

        with self.test_ass.open("r", encoding='ascii') as f:
            with self.assertRaises(ValueError):
                ass.parse(f)


if __name__ == "__main__":
    unittest.main()
