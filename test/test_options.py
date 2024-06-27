# coding: utf-8

from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_dl.options import _hide_login_info


class TestOptions(unittest.TestCase):
    def test_hide_login_info_basic(self):
        self.assertEqual(
            _hide_login_info(['-u', 'foo', '-p', 'bar']),
            ['-u', 'PRIVATE', '-p', 'PRIVATE']
        )

    def test_hide_login_info_one_random(self):
        self.assertEqual(_hide_login_info(['-u']), ['-u'])

    def test_hide_login_info_multiple_users(self):
        self.assertEqual(
            _hide_login_info(['-u', 'foo', '-u', 'bar']),
            ['-u', 'PRIVATE', '-u', 'PRIVATE']
        )

    def test_hide_login_info_long(self):
        self.assertEqual(
            _hide_login_info(['--username=foo']),
            ['--username=PRIVATE']
        )

    def test_hide_login_info_password(self):
        self.assertEqual(
            _hide_login_info(['--password=bar']),
            ['--password=PRIVATE']
        )

    def test_hide_login_info_combined(self):
        self.assertEqual(
            _hide_login_info(['-u', 'foo', '--password=bar']),
            ['-u', 'PRIVATE', '--password=PRIVATE']
        )

    def test_hide_login_info_irrelevant_things(self):
        self.assertEqual(
            _hide_login_info(['-v', '--help']),
            ['-v', '--help']
        )

    def test_hide_login_info_empty(self):
        self.assertEqual(_hide_login_info([]), [])

if __name__ == '__main__':
    unittest.main()
