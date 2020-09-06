# -*- coding: utf-8 -*-

import unittest
from main import main

class TestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello world!")

if __name__ == "__main__":
    unittest.main()
