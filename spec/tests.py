import sys
import unittest

from diskspace.diskspace import *
import subprocess

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


