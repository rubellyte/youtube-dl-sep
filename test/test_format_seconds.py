import unittest
from youtube_dl.utils import formatSeconds, formatSeconds_branch_coverage

class TestFormatSeconds(unittest.TestCase):

    def setUp(self):
        formatSeconds_branch_coverage.update({
            "more_than_hour": False,
            "between_minute_and_hour": False,
            "less_than_minute": False
        })

    def tearDown(self):
        print(formatSeconds_branch_coverage)

    def test_format_less_than_minute(self):
        self.assertEqual(formatSeconds(1), "1")
        self.assertEqual(formatSeconds(0), "0")
        self.assertEqual(formatSeconds(-1), "-1")
        self.assertEqual(formatSeconds(59), "59")
        self.assertEqual(formatSeconds(60), "60")

    def test_format_minute_to_hour(self):
        self.assertEqual(formatSeconds(61), "1:01")
        self.assertEqual(formatSeconds(60.0001), "1:00")
        self.assertEqual(formatSeconds(600), "10:00")
        self.assertEqual(formatSeconds(3599), "59:59")
        self.assertEqual(formatSeconds(3600), "60:00")

    def test_format_more_than_hour(self):
        self.assertEqual(formatSeconds(3601), "1:00:01")
        self.assertEqual(formatSeconds(3600.0001), "1:00:00")
        self.assertEqual(formatSeconds(36000), "10:00:00")
        self.assertEqual(formatSeconds(360000), "100:00:00")

if __name__ == '__main__':
    unittest.main()
    print(formatSeconds_branch_coverage)