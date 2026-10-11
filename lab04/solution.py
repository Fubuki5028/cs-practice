def winner(names : list[str], scores: list[float]) -> str:
    max_score = float('-inf')
    for i in range(len(scores)):
        if max_score < scores[i]:
            max_score = scores[i]
            win = names[i]
    return win

def average(scores: list[float]) -> float:
    avg = 0.0 
    for i in range(len(scores)):
        avg += scores[i]
    return avg / len(scores)
