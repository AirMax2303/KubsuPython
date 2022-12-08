import random

words = {
    "привет": "hello",
    "мир": "world",
    "яблоко": "apple",
    "кольцо": "ring",
    "пуля": "bullet",
    "машина": "car",
    "студент": "student",
}

list_word= []

def get_word():
    check_true = False
    _word = list(words.items())[random.randint(0, len(words)-1)]
    while check_true == False:
        if _word in list_word:
            _word = list(words.items())[random.randint(0, len(words)-1)]
        else:
            check_true == True
            list_word.append(_word)
            break
    return _word

errors = 0
correct_answer = 0
while errors < 2 and correct_answer <= len(words):
    eng, rus = get_word()
    if input("%s = " % eng).lower() == rus:
        print("Верно")
        correct_answer += 1
    else:
        print("Не верно.")
        errors += 1
if errors == 2:
    print("Вы проиграли!")
else:
    print("Вы выиграли!")
