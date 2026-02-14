from decimal import Decimal


class LogPrinter:

    def __init__(self, column_headers=None, data=None, decimals=None, prefix=None, suffix=None, align=None):
        self.column_headers = column_headers
        self.data = data if data is not None else [[]]
        self.decimals = decimals
        self.prefix = prefix
        self.suffix = suffix
        self.align = align

    def print(self):
        if self.column_headers is None:
            combined_array = self.data
        else:
            combined_array = [self.column_headers] + self.data
        table = self.format_table(combined_array, self.decimals, self.prefix, self.suffix, self.align)
        print(f"{table}")

    @staticmethod
    def format_cell(cell, decimals=None, prefix=None, suffix=None):
        if decimals is not None and isinstance(cell, (int, float, Decimal)):
            cell = f"{cell:.{decimals}f}"
        if prefix is not None:
            cell = str(prefix) + str(cell)
        if suffix is not None:
            cell = str(cell) + str(suffix)
        return str(cell)

    @staticmethod
    def pad_array(arr):
        max_len = max(len(row) for row in arr)
        padded_arr = []
        for row in arr:
            padded_row = row + [''] * (max_len - len(row))
            padded_arr.append(padded_row)
        return padded_arr

    @staticmethod
    def _normalize_options(options, max_len, default_value):
        if options is None:
            return [default_value] * max_len
        if isinstance(options, (int, str)):
            return [options] * max_len
        options = list(options)
        if len(options) < max_len:
            options.extend([default_value] * (max_len - len(options)))
        return options[:max_len]

    @staticmethod
    def _split_lines(cell_string):
        return cell_string.split("\n")

    @staticmethod
    def _align_cell(text, width, alignment):
        if alignment == "left":
            return text.ljust(width)
        if alignment == "right":
            return text.rjust(width)
        return text.center(width)

    def format_table(self, data, decimals=None, prefix=None, suffix=None, align=None):
        data = self.pad_array(data)
        max_row_length = max(len(row) for row in data) if data else 0
        decimals = self._normalize_options(decimals, max_row_length, None)
        prefix = self._normalize_options(prefix, max_row_length, None)
        suffix = self._normalize_options(suffix, max_row_length, None)
        align = self._normalize_options(align, max_row_length, "center")

        formatted_cells = []
        for row in data:
            formatted_row = []
            for i, cell in enumerate(row):
                if self.column_headers is not None and row is data[0]:
                    formatted_row.append(str(cell))
                else:
                    formatted_row.append(self.format_cell(cell, decimals[i], prefix[i], suffix[i]))
            formatted_cells.append(formatted_row)

        column_widths = [0] * max_row_length
        for row in formatted_cells:
            for i, cell in enumerate(row):
                lines = self._split_lines(cell)
                max_len = max(len(line) for line in lines) if lines else 0
                if max_len > column_widths[i]:
                    column_widths[i] = max_len

        divider = "+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+"

        rows = []
        for row_index, row in enumerate(formatted_cells):
            split_cells = [self._split_lines(cell) for cell in row]
            row_height = max(len(lines) for lines in split_cells) if split_cells else 1
            for line_index in range(row_height):
                line_parts = []
                for col_index, lines in enumerate(split_cells):
                    text = lines[line_index] if line_index < len(lines) else ""
                    aligned = self._align_cell(text, column_widths[col_index], align[col_index])
                    line_parts.append(f"| {aligned} ")
                rows.append("".join(line_parts) + "|")

            if self.column_headers is not None and row_index == 0:
                rows.append(divider)

        if self.column_headers is not None:
            table_string = divider + "\n" + "\n".join(rows) + "\n" + divider
        else:
            table_string = divider + "\n" + "\n".join(rows) + "\n" + divider
        return table_string
