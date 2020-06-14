with open("score.csv", "r", encoding="utf-8") as fp:

    context = fp.readlines()

    total = []
    for i in range(len(context)):
        print("{}번째: {}".format(i+1, context[i]))
        
        student = context[i].split(',')
        korean = int(student[2])
        english = int(student[3])
        math = int(student[4])
        total.append(korean + english + math)
        evg = total[i] / 3

        #fp.write(total[i])
        #fp.write(evg)

    rank = []
    for i in range(len(total)):
        r = 1
        for j in range(len(total)):
            if total[i] < total[j]:
                r += 1
        rank.append(r)
    
    print(rank)

    