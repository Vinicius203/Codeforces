num_cases = int(input())


def codifica(word):
    new_word = word[0] + str((len(word) - 2)) + word[len(word)-1]
    return new_word


for i in range(0, num_cases):
    word = input()
    if (len(word) <= 10):
        print(word)
    else:
        print(codifica(word))
