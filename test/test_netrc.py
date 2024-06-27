# coding: utf-8
from __future__ import unicode_literals

import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_dl.extractor import gen_extractors

class TestNetRc(unittest.TestCase):
    def test_netrc_present(self):
        extractors_with_login = []
        extractors_without_login = []
        
        for ie in gen_extractors():
            if hasattr(ie, '_login'):
                extractors_with_login.append(ie)
                self.assertTrue(
                    hasattr(ie, '_NETRC_MACHINE'),
                    'Extractor %s supports login, but is missing a _NETRC_MACHINE property' % ie.IE_NAME
                )
                self.assertTrue(
                    isinstance(ie._NETRC_MACHINE, str) and ie._NETRC_MACHINE,
                    'Extractor %s has an invalid _NETRC_MACHINE property' % ie.IE_NAME
                )
            else:
                extractors_without_login.append(ie)
        
        print(f"Checked {len(extractors_with_login)} extractors with login support.")
        print(f"Checked {len(extractors_without_login)} extractors without login support.")

if __name__ == '__main__':
    unittest.main()
