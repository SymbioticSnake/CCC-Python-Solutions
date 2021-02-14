def track_score():
    score = 0
    for multi in range(3, 0, -1):
        score += multi * int(input())
    
    return score

apples = track_score()
bananas = track_score()

if apples > bananas: print("A")
elif bananas > apples: print("B")
else: print("T")