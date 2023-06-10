# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго 
# множества. Затем пользователь вводит сами элементы множеств.

n = int (input("Enter n number: "))
m = int (input("Enter m number:" ))
List_1 = []
List_2 = []
for i in range (n):
    List_1.append(int (input("Enter an element of the first set")))
for i in range (m):  
    List_2.append(int (input("Enter an element of the second set")))
List_1 = set(List_1)
List_2 = set(List_2)
List_3 = (List_1.intersection(List_2))
print(sorted(List_3))


