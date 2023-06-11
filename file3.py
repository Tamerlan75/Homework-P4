# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго 
# множества. Затем пользователь вводит сами элементы множеств.

# n = int (input("Enter n number: "))
# m = int (input("Enter m number:" ))
# List_1 = []
# List_2 = []
# for i in range (n):
#     List_1.append(int (input("Enter an element of the first set")))
# for i in range (m):  
#     List_2.append(int (input("Enter an element of the second set")))
# List_1 = set(List_1)
# List_2 = set(List_2)
# List_3 = (List_1.intersection(List_2))
# print(sorted(List_3))

# 2. На круглой грядке растёт N кустов, на i-ом кусте выросло ai ягод. 
# За один заход собираются ягоды с трех кустов. Найти максимальное число ягод, собираемых за один заход. 

# n = 13 
# List_g = [35,56,48,39,54,43,61,59,46,51,49,20,23]
# List_s = []
# for i in range(2,len(List_g), 3):
#     List_s.append(List_g[i] + List_g[i-1] + List_g[i-2])
# if len(List_g)%3 == 2:
#     List_s.append(List_g[-2]+List_g[-1])
# if len(List_g)%3 == 1:
#     List_s.append(List_g[-1])
# print(List_s,"=>",max(List_s))




# 3. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов 
# идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

# text = input ("Введите текст: ")
# count = 1
# for i in text:
#     if i == " ":
#         count+=1
# print(count)

