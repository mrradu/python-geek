__author__ = 'Карунту Родион'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
num = input('Введите число: ')
i = 0
while i <len(num):
	print(int(num) // 10 ** i % 10)
	i+=1



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

x = int(input("Введите первое значение:"))
y = int(input("Введите первое значение:"))

#x *= y
#y = x / y
#x /=y

z = x
x = y
y = z

print("Первое значение: ", x)
print("Второе значение: ", y)
# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Введите ваш возраст:"))

if age >=18:
	print("Доступ разрешен")
else:
	print("Извините, пользование данным ресурсом только с 18 лет")