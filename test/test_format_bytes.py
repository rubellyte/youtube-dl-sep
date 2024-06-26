import unittest
from youtube_dl.utils import format_bytes, format_bytes_branch_coverage

class TestFormatBytes(unittest.TestCase):

    def setUp(self):
        format_bytes_branch_coverage.update({
            "none_bytes": False,
            "bytes_is_str": False,
            "bytes_equal_zero": False,
            "bytes_not_equal_zero": False
        })

    def tearDown(self):
        print(format_bytes_branch_coverage)

    def test_format_bytes(self):
        self.assertEqual(format_bytes(0), "0.00B")
        self.assertEqual(format_bytes(1), "1.00B")
        self.assertEqual(format_bytes(1023), "1023.00B")
        self.assertEqual(format_bytes(1024), "1.00KiB")
        self.assertEqual(format_bytes(1024 ** 2), "1.00MiB")
        self.assertEqual(format_bytes(1024 ** 3), "1.00GiB")
        self.assertEqual(format_bytes(1024 ** 4), "1.00TiB")
        self.assertEqual(format_bytes(1024 ** 5), "1.00PiB")
        self.assertEqual(format_bytes(1024 ** 6), "1.00EiB")
        self.assertEqual(format_bytes(1024 ** 7), "1.00ZiB")
        self.assertEqual(format_bytes(1024 ** 8), "1.00YiB")

    def test_format_bytes_none(self):
        self.assertEqual(format_bytes(None), "N/A")

    def test_format_bytes_string(self):
        self.assertEqual(format_bytes("1"), "1.00B")
        with self.assertRaises(ValueError):
            format_bytes("not a number")