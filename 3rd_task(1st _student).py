# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:59:15 2023

@author: admin
"""

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

ed, exp = 10000, 12000

m = 1
d = exp - ed
while m < 10:
    m+= 1
    exp *= 1.03
    #peremesheno ispravleno
    d += exp - ed
    #chtob ispravit oshibku na programme nado vpervo postavit
    #komandu uvelechenie rasxodi pered vichitanie raznitsu
            
d = round(d, 2)
print('Студенту надо попросить', d, 'рублей.')



#perviy student reshil zadachu pochti pravilno, to'ko u nego
#perviy nado bilo postavit exp *=1.03 pered d+ = exp -ed