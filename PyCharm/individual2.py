sentence = input("Введите предложение: ")
if 'чу' in sentence:
    print('чу найдено на позиции', sentence.index('чу')+1)
elif 'щу' in sentence:
    print('щу найдено на позиции', sentence.index('щу')+1)
else:
    print('Буквосочетания не найдены.')
