import os
import tempfile
import unittest

from jm_tools.lazy_keystore import LazyCsvStore


class TestLazyCsvStore(unittest.TestCase):
    def _write_sample(self, filename):
        with open(filename, "w") as file:
            file.write("id,value\n")
            file.write("a,1\n")

    def test_update_single_record_missing_key(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            filename = os.path.join(tmp_dir, "data.csv")
            self._write_sample(filename)

            store = LazyCsvStore(filename, headers=["id", "value"])
            store.update_single_record("missing", {"id": "missing", "value": "2"})

            temp_filename = filename.replace(".csv", "_temp.csv")

            self.assertFalse(os.path.exists(temp_filename))

            with open(filename, "r") as file:
                contents = [line.strip() for line in file.readlines() if line.strip()]

            self.assertEqual(contents, ["id,value", "a,1"])

    def test_update_single_record_existing_key(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            filename = os.path.join(tmp_dir, "data.csv")
            self._write_sample(filename)

            store = LazyCsvStore(filename, headers=["id", "value"])
            store.update_single_record("a", {"id": "a", "value": "2"})

            with open(filename, "r") as file:
                contents = [line.strip() for line in file.readlines() if line.strip()]

            self.assertEqual(contents, ["id,value", "a,2"])


if __name__ == "__main__":
    unittest.main()
