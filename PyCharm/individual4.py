word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

can_form = True
for letter in word2:
    if letter not in word1:
        can_form = False
        break

if can_form:
    print("Можно сформировать второе слово из букв первого")
else:
    print("Невозможно сформировать второе слово из букв первого")
