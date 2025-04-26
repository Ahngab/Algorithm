def solution(cards1, cards2, goal):
    idx1, idx2, Idx = 0, 0, 0
    flag = 1
    while Idx < len(goal):
        if idx1 < len(cards1) and goal[Idx] == cards1[idx1]:
            idx1 += 1
            Idx += 1
        elif idx2 < len(cards2) and goal[Idx] == cards2[idx2]:
            idx2 += 1
            Idx += 1
        else:
            flag = 0
            break

    if flag:
        return "Yes"
    else:
        return "No"