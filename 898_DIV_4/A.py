cases_quantity = int(input())


def possible(string):
    if string[0] == "a" or string[1] == "b" or string[2] == "c":
        return "YES"

    return "NO"


for i in range(0, cases_quantity):
    string_row = input()
    result = possible(string_row)
    print(result)
