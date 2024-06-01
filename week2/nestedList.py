if __name__ == '__main__':
    d = {}
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score
        scores.append(score)
    
    unique_scores = list(set(scores))
    unique_scores.sort()
    # print(unique_scores)
    second_lowest = unique_scores[1]
    
    second_lowest_names = [name for name, score in d.items() if score == second_lowest]
    
    for name in sorted(second_lowest_names):
        print(name)
