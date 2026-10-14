def winner(names, scores):
    max_score = float('-inf')
    for i in range(len(scores)):
        if max_score < scores[i]:
            max_score = scores[i]
            win = names[i]
    return win

def average(scores):
    if not scores:
        return 0.0
    avg = 0.0
    for i in range(len(scores)):
        if scores[i] != None:
            avg += scores[i]
    return round(avg / len(scores), 2)

def ranking(names, scores):
    comb = list(zip(names,scores))
    comb.sort(key = lambda x: x[1], reverse = True)
    return [x for x, y in comb]

def above_average(names, scores):
    abv_avg = []
    for i in range(len(scores)):
        if average(scores) < scores[i]:
            abv_avg.append(names[i])
    return abv_avg

if __name__ == "__main__":
    print(winner(["Аня", "Боря", "Вика"],[7.0,   9.0,    9.0]))
    print(average([7.0,   9.0,    9.0]))
    print(ranking(["Аня", "Боря", "Вика"],[7.0,   9.0,    9.0]))
    print(above_average(["Аня", "Боря", "Вика"],[7.0,   9.0,    9.0]))
    print(average([None, 3, 3]))
