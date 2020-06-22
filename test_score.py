from std_score import Score
from unittest import TestCase

class Myscore(TestCase):   
    
    def test_openfile_result(self):
        a = Score()
        a.open_file()
        a.context

        fp = open("score.csv", "r", encoding="utf-8")
        context_csv = fp.readlines()
        fp.close()

        self.assertListEqual(a.context, context_csv)

    def test_score_resutl(self):
        context = Score.open_file(0)
        student1 = context[0]
        std_list = student1.split(",")
        korean = int(std_list[2])
        self.assertEqual(korean, 85)

    def test_construtor(self):
        scr = Score()
        self.assertIsNotNone(scr)