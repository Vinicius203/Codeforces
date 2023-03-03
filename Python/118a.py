def replaceVowels(word, vowels):

    for letra in vowels:
        word = word.replace(letra, '')

    return word

word = input()

word_lower = word.lower()
vowels = 'aeiouy'

word_lower = replaceVowels(word_lower, vowels)
word_final = ''

for letra in word_lower:
    word_final += f'.{letra}'

print(word_final)