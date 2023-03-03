numero = input()

cont_lucky_numbers = 0

for num in numero:
    if num == '4' or num == '7':
        cont_lucky_numbers += 1

if (cont_lucky_numbers == 4 or cont_lucky_numbers == 7):
    print('YES')
else:
    print('NO')
