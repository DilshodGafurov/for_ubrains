# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:07:38 2023

@author: admin
"""

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом


#user_input = input("Введите, пожалуйста, номер месяца: ")
#month = int(user_input)
#print('Вы ввели', month)
#if month == 1:
#    print('31 день')
#elif month == 2:
#    print('28 дней')
#elif month == 3:
#    print('31 день')
#elif month == 4:
#    print('30 дней')
#elif month == 5:
#    print('31 день')
#elif month == 6:
#    print('30 дней')
#elif month == 7:
#    print('31 день')
#elif month == 8:
#    print('31 день')
#elif month == 9:
#    print('30 дней')
#elif month == 10:
#    print('31 день')
#elif month == 11:
#    print('30 дней')
#elif month == 12:
#    print('31 день')
#else:
#    print('Такого месяца нет')
 
   
#reshenie pravilno
#mojno i bilo reshat s pomoshyu listom

month = [31,28,31,30,31,30,31,31,30,31,30,31]
user_input = int(input("Введите, пожалуйста, номер месяца: "))
if (user_input > 12 or user_input <= 0):
    print('Такого месяца нет')
else:
    print(f"Вы ввели, {user_input}, на нём {month[user_input-1]} дней")