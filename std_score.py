class Score:
    total = []
    avg = []

    def open_file(self):
        fp = open("score.csv", "r", encoding="utf-8")
        context = fp.readlines()
        fp.close()
        return context
    
    def get_score(self):
        context = self.open_file()
        context = Score.open_file(0)
        student1 = context[0]
        std_list = student1.split(",")
        korean = std_list[2]
        print(korean)
        for i in range(len(context)):
            student = context[i].split(',')
            korean = int(student[2])
            english = int(student[3])
            math = int(student[4])
            self.total.append(korean + english + math)
            self.avg.append(round(self.total[i] / 3, 2))
        return

a = Score()
a.get_score()