# my_list = []   # или нужно использовать my_list = list() #print(my_list[1])
# range(5) --> [0, 1, 2, 3, 4]
# range(5, 11) --> [5, 6, 7, 8, 9, 10]
# range(5, 11, 2) где двойка это перебор на чётные

# for i in range(5): 
   # x = int(input('---> '))
   # my_list.append(x)        # команда для ввода своих чисел в масив
# print(my_list)

# удалить элемент можно сследующим образом
# my_list = [1, 2, 3]
# my_list.pop(1)
# print(my_list)
# my_list.remove(2)
# print(my_list )

# Поиск макимального числа 
# max = 0 
# for i in range(5):
#    x = int(input('--> '))
#    if i == 0:
#       max = x
#    elif x > max:
#       max = x
# print(max)

# решение через while
my_list = [5, 2, 9, 1, 3]
i = 1
max = my_list[0]
while i < len(my_list):
   if my_list[i] > max:
      max = my_list[i]
   i += 1
print(max)

