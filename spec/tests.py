import sys
import unittest

from diskspace.diskspace import *
import os

class Test(unittest.TestCase):
    def test_bytes_to_readable(self):
        blocks = 1
        result = '512.00B'
        self.assertEquals(result, bytes_to_readable(blocks))

        blocks = 2
        result = '1.00Kb'
        self.assertEquals(result, bytes_to_readable(blocks))
        
        blocks = 100
        result = '50.00Kb'
        self.assertEquals(result, bytes_to_readable(blocks))

    def test_show_space_list(self):
        self.assertIsNone(show_space_list())

    def test_subprocess_check_output(self):
        func = subprocess_check_output('pwd')
        cwd = os.getcwd()+'\n'
        self.assertEquals(cwd, func)