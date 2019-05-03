#!/usr/bin/env python

import ass
import unittest
from pathlib import Path

from io import StringIO

folder = Path(__file__).parent


class TestEverything(unittest.TestCase):
    def test_parse_dump(self):

        with Path(folder, "test.ass").open("r", encoding='utf_8_sig') as f:
            contents = f.read()

        doc = ass.parse(StringIO(contents))
        out = StringIO()
        doc.dump_file(out)

        assert out.getvalue().strip() == contents.strip()


if __name__ == "__main__":
    unittest.main()
