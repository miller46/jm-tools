# Install Guide

```bash
pip install jm-tools
```

# Log Printer

Quickly format tabular data for logs with per-column alignment and formatting.

```python
from jm_tools.log_printer import LogPrinter

headers = ["Name", "Price", "Change"]
rows = [
    ["ETH", 1234.56, "+1.2%"],
    ["BTC", 65432.1, "-0.8%"],
]

printer = LogPrinter(
    column_headers=headers,
    data=rows,
    decimals=[None, 2, None],
    align=["left", "right", "center"],
)
printer.print()
```

Notes:
- `align` accepts `left`, `center`, or `right` per column.
- `decimals`, `prefix`, and `suffix` accept a single value or a list per column.
- Multi-line cells are supported and keep table borders aligned.

# Build Pip Package
```bash
python setup.py sdist
```
