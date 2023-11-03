cases_quantity = int(input())

for _ in range(cases_quantity):
    digits = list(map(int, input().split()))
    digits_list_sorted = sorted(digits)
    del digits_list_sorted[0]
    if sum(digits_list_sorted) >= 10:
        print("YES")
        continue
    print("NO")
