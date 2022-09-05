q = {
    "madre": [
        "мама",
        "мать"
    ],
    "padre": [
        "папа",
        "батя"
    ],
    "sorella": [
        "сестра"
    ],
    "bratello": [
        "брат"
    ]
}

while True:
    print("Введите слово или уходите, для этого напишите 'exit'")
    a = input()
    if a == "exit":
        print("Операция завершена")
        break
    if a in q:
        print("Введено слово", a, "перевод слова", " или ".join(q.get(a)))
    if a not in q:
        print("Слово не найдено")
