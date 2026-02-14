import unittest

from jm_tools.log_printer import LogPrinter


class TestLogPrinter(unittest.TestCase):
    def test_mutable_defaults_are_not_shared(self):
        lp1 = LogPrinter()
        lp2 = LogPrinter()
        lp1.data.append(["x"])
        self.assertEqual(lp2.data, [[]])

    def test_alignment_per_column(self):
        data = [["a", "bb", "ccc"]]
        lp = LogPrinter(column_headers=None, data=data, align=["left", "center", "right"])
        table = lp.format_table(data, align=["left", "center", "right"])
        lines = table.split("\n")

        row = lines[1]

        self.assertIn("| a ", row)
        self.assertRegex(row, r"\|\s+bb\s+\|")
        self.assertIn(" ccc |", row)

    def test_options_shorter_than_columns(self):
        data = [[1, 2, 3]]
        lp = LogPrinter(column_headers=None, data=data, decimals=[2])
        table = lp.format_table(data, decimals=[2])

        self.assertIn("1.00", table)
        self.assertIn("2", table)
        self.assertIn("3", table)

    def test_multiline_cells_do_not_break_pipes(self):
        data = [["a\nb", "c"]]
        lp = LogPrinter(column_headers=None, data=data)
        table = lp.format_table(data)
        lines = table.split("\n")

        self.assertEqual(len(lines), 4)
        for line in lines[1:3]:
            self.assertEqual(line.count("|"), 3)


if __name__ == "__main__":
    unittest.main()
