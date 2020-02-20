import keyword

def validate():
    while True:
        strInput = input("Ввод=> ")
        if(len(strInput)==0):
            print("Ошибка!Вы ничего не ввели!")
            return
        if(keyword.iskeyword(strInput)):
            print("NOK: ключевое слово")

        if(strInput[0]=="_" and strInput[1]=="_"):
             print("OK: так называют приватные идентификаторы")

        if(strInput[0].isdigit()):
            print("NOK: начинается с цифры")

        if(strInput == strInput.upper()):
            print("OK: так называют константы")

        if(strInput[0] == strInput.upper()[0]  and strInput[0].isalpha() and strInput.swapcase() != strInput):
            print("OK: так называют классы")

        if (strInput.lower() == strInput and strInput[0].isalpha()):
            print("OK: так называют переменные")

        if(strInput[0]=="_"):
            print("OK: так называют защищенные идентификаторы")


validate()