numero = int(input())

sequencia = input()
anton_win = 0
danik_win = 0

for vitoria in sequencia:
    if vitoria == 'A':
        anton_win += 1
    else:
        danik_win += 1

if anton_win > danik_win:
    print('Anton')
elif anton_win < danik_win:
    print('Danik')
else:
    print('Friendship')
