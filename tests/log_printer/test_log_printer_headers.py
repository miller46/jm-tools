import unittest

from jm_tools.log_printer import LogPrinter


class TestLogPrinterHeaders(unittest.TestCase):
    def test_header_divider_inserted_once(self):
        headers = ["col1", "col2"]
        data = [["a", "b"], ["c", "d"]]
        lp = LogPrinter(column_headers=headers, data=data)
        table = lp.format_table([headers] + data)
        lines = table.split("\n")

        self.assertEqual(lines[0], lines[2])
        self.assertEqual(lines[2], lines[-1])
        self.assertEqual(len(lines), 6)

    def test_header_respects_alignment(self):
        headers = ["left", "center", "right"]
        data = [["a", "b", "c"]]
        align = ["left", "center", "right"]
        lp = LogPrinter(column_headers=headers, data=data, align=align)
        table = lp.format_table([headers] + data, align=align)
        header_row = table.split("\n")[1]

        self.assertIn("| left ", header_row)
        self.assertRegex(header_row, r"\|\s+center\s+\|")
        self.assertIn(" right |", header_row)


if __name__ == "__main__":
    unittest.main()
