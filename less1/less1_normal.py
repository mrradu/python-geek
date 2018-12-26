
__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

num = input('Введите число: ')
i = 0
prom = 0
while i <len(num):
	num_now = int(num) // 10 ** i % 10
	if prom < num_now:
		prom = num_now
	i+=1
print(prom)




# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

x = int(input("Введите первое значение:"))
y = int(input("Введите первое значение:"))

x,y = y,x

print("Первое значение: ", x)
print("Второе значение: ", y)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

a = int(input('Введите a '))
b = int(input('Введите b '))
c = int(input('Введите c '))
D = (b ** 2) - (4 * a * c)
if D > 0:
	x1 = ((- b) - (D ** 0.5)) / (2 * a)
	x2 = ((- b) + (D ** 0.5)) / (2 * a)
	print('X1 =', x1)
	print('X2 =', x2)
elif D == 0:
	x1 = (- b) / (2 * a)
	print('Уравнение имеет один корень X = ', x1)
elif D < 0:
	print(D)
	print('Уравнение не имеет корней')
