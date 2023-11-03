cases_quantity = int(input())


def find_add(digit_list):
    min_value = float("inf")
    min_index = -1
    for i, num in enumerate(digit_list):
        if num < min_value:
            min_value = num
            min_index = i

    digit_list[min_index] += 1
    result = 1
    for num in digit_list:
        result *= num

    return result


for _ in range(cases_quantity):
    digits_quantity = int(input())
    digits = list(map(int, input().split()))
    result = find_add(digits)
    print(result)
