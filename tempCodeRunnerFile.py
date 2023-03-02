from collections import Counter

num_cases = int(input())


def beautifulCounter(tower_colors):
    beautiful_counter = 0
    for i in range(0, len(tower_colors) - 1):
        if tower_colors[i] != tower_colors[i+1]:
            beautiful_counter += 1
    return beautiful_counter


def colorCounter(tower1_colors, tower2_colors):
    rCounter = 0
    bCounter = 0

    rCounter = Counter(tower1_colors) + Counter(tower2_colors)
    bCounter = Counter(tower1_colors) + Counter(tower2_colors)

    x = abs(rCounter['R'] - bCounter['B'])
    return x


for i in range(0, num_cases):
    check = 0
    tower1_size, tower2_size = input().split()
    tower1_colors = input()
    tower2_colors = input()

    if (len(tower1_colors) != 1 or len(tower2_colors) != 1):
        check = colorCounter(tower1_colors, tower2_colors)

    if check > 1:
        print('NO')

    else:
        beautiful_counter = beautifulCounter(
            tower1_colors) + beautifulCounter(tower2_colors)

        if beautiful_counter == (len(tower1_colors) - 1) + (len(tower2_colors)-1):
            print('YES')
        elif tower1_colors[len(tower1_colors)-1] != tower2_colors[len(tower2_colors)-1]:
            print('YES')
        else:
            print('NO')
