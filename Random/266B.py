children_number, seconds = map(int, input().split())
row = input()
seconds_aux = 0

while seconds_aux < seconds:
    row_list = list(row)  # Convert the string to a list to modify individual characters
    for position in range(len(row_list) - 1):
        if row_list[position] == "B" and row_list[position + 1] == "G":
            row_list[position], row_list[position + 1] = (
                row_list[position + 1],
                row_list[position],
            )
    row = "".join(row_list)  # Convert the modified list back to a string
    seconds_aux += 1

print(row)
