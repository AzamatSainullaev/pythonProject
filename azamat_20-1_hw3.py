# Программа должна работать в бесконечном цикле с возможностью выхода
# Запрашивать у пользователя любое слово на латинице или кириллице
while True:
    a = input("Введите слово: ")

    if a == "123":
        break
# Вывести общее количество букв в данном слове
    print("Количество букв", len(a))

# Считывать строчные и прописные буквы
    vowels = 0
    consonants = 0
    for i in a:
        letter = i.lower()
        if letter == "a" or letter == "e" or letter == "а" or letter == "У" or letter == "о" or\
           letter == "i" or letter == "o" or letter == "ы" or letter == "э" or letter == "я" or\
           letter == "u" or letter == "y" or letter == "ю" or letter == "е" or letter == "ё" or \
           letter == "и":
            vowels += 1
        else:
            consonants += 1

# Вывести количество согласных и гласных букв
    print("Гласные %i\n""Согласные %i" % (vowels, consonants))

# Вывести процентное соотношение гласных и согласных букв до двух цифр после точки
    print(f'Гласные = {round(vowels / len(a) * 100, 2)}%', f'Согласные = {round(consonants / len(a) * 100, 2)}%')





