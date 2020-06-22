class Score:
    total = []
    avg = []
    rank = []
    context = []

    def open_file(self):
        fp = open("score.csv", "r", encoding="utf-8")
        self.context = fp.readlines()
        fp.close()
        return
    
    def get_score(self):
        for i in range(len(self.context)):
            student = self.context[i].split(',')
            korean = int(student[2])
            english = int(student[3])
            math = int(student[4])
            self.total.append(korean + english + math)
            self.avg.append(round(self.total[i] / 3, 2))
        return

    def write_file(self):
        for score1 in self.total:
            r = 1
            for score2 in self.total:
                if score1 < score2:
                    r += 1
            self.rank.append(r)

        with open("result.csv", "w", encoding="utf-8") as wf:
            for i in range(len(self.context)):
                wf.write(self.context[i].replace('\n','') + ',')
                wf.write(self.total[i].__str__() + ',')
                wf.write(self.avg[i].__str__() + ',')
                wf.write(self.rank[i].__str__() + '\n')
        return

a = Score()
a.open_file()
a.get_score()
a.write_file()