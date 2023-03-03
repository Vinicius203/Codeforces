def alfabetica(string1, string2):
    if string1 < string2:
        return -1
    elif string1 > string2:
        return 1
    else:
        return 0


string1 = input()
string2 = input()

string1_upper = string1.upper()
string2_upper = string2.upper()

print(alfabetica(string1_upper, string2_upper))
