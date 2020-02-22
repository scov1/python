import keyword


def validate():
    while True:
        text = input("Ввод=> ")
        if len(text) == 0:
            print("Ошибка!Вы ничего не ввели!")
            return
        if (keyword.iskeyword(text)):
            print("NOK: ключевое слово")

        elif (text[0] == "_" and text[1] != "_"):
            print("OK: так называют защищенные идентификаторы")

        elif (text[0] == "_" and text[1] == "_"):
            print("OK: так называют приватные идентификаторы")

        elif (text[0].isdigit()):
            print("NOK: начинается с цифры")

        elif (text == text.upper()):
            print("OK: так называют константы")

        elif (text[0] == text.upper()[0] and text[0].isalpha() and text.swapcase() != text):
            print("OK: так называют классы")

        elif (text.lower() == text and text[0].isalpha()):
            print("OK: так называют переменные")


validate()
