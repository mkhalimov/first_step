def battle(orcs, h):
    if h == 3 and orcs >= 85: 
        return 1
    elif h == 3 and orcs < 85:
        return 0
    elif orcs >= 85 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return battle(orcs + 1, h + 1) or battle(orcs * 2, h + 1) or battle(orcs + 3, h + 1) or battle(orcs * 3, h + 1)
        else:
             return battle(orcs + 1, h + 1) or battle(orcs * 2, h + 1) or battle(orcs + 3, h + 1) or battle(orcs * 3, h + 1)

for orcs in range(1, 42):
    if battle(orcs, 1) == 1:
        print("Задача 19: ", orcs)
        break
