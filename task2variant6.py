# С клавиатуры вводится текст, определить, сколько в нем гласных
# а сколько согласных. В случае равенства вывести на экран все
# согласные буквы. Посчитать количество слов в тексте

text = input("Введите ваш текст: ").lower()

vovels = 0
consonants = 0
consonants_letters = []

for letter in text:
    if letter.isalpha():
        if letter in "ёуеыаояиюэaeiouy":
            vovels += 1
        else:
            consonants += 1
            consonants_letters.append(letter)
words = len(text.split())

print(f"Количество гласных: {vovels}")
print(f"Количество согласных: {consonants}")

if vovels == consonants:
    # print("Согласные буквы: ", "".join(consonants_letters))
    print(f"Согласные буквы: {consonants_letters}")
print(f"Количество слов в тексте: {words}")
