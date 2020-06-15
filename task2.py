"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def funct(arg1,arg2):
    if type(arg1) is not str or type(arg2) is not str:
        return 0
    if arg1.lower() == arg2.lower():
        return 1
    if len(arg1) > len(arg2):
        if arg2=="learn":
            return 3
        else:
            return 2
    if arg2=="learn" and arg1 != arg2:
        return 3




def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(funct(1,4))
    print(funct("Hello","hello"))
    print(funct("Hello222","Hello1"))
    print(funct("Hello33","learn"))
    print(funct("Hello","Hello123"))
    print(funct("Hi","learn"))
    
if __name__ == "__main__":
    main()
