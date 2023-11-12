word = input("Введите слово: ")
position = 5
letter = 'т'

if position < len(word):
    new_word = word[:position] + letter + word[position:]
    print(new_word)
else:
    print("Позиция вне диапазона слова")
