import unittest
from unittest import TestCase

class Score:
    def openfile(self):
        fp = open("score.csv", "r", encoding="utf-8")
        context = fp.readlines()
        return context
    
    def test_construtor(self):
        scr = Score()
        self.assertIsNotNone(scr)

if __name__ == "__main__"'''''''':
    unittest.main()
