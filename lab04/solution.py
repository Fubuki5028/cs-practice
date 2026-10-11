def winner(names : list[str], scores: list[float]) -> str:
    max_score = float('-inf')
    for i in range(len(scores)):
        if max_score < scores[i]:
            max_score = scores[i]
            win = names[i]
    return win

def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    avg = 0.0
    for i in range(len(scores)):
        avg += scores[i]
    return round(avg / len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    comb = list(zip(names,scores))
    comb.sort(key = lambda x: x[1], reverse = True)
    return [x for x, y in comb]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    abv_avg = []
    for i in range(len(scores)):
        if average(scores) < scores[i]:
            abv_avg.append(names[i])
    return abv_avg