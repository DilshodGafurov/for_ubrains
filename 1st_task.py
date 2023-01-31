# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:44:40 2023

@author: admin

Задание 1. Проанализируйте код.
operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '**': lambda a, b: a ** b,
    '/': lambda a, b: a / b,
    '//': lambda a, b: a // b,
    '%': lambda a, b: a % b
}

spam = operators.get('+')
print(spam(1, 2))

Перепишите код с использованием парадигмы ООП.
Требования к решению.
Код соответствует РЕР8.
Код имеет модульную структуру.
Используется type hinting (typing, collections.abc).
Особое внимание уделите неймингу.
Код отвечает рекомендациям SOLID.
Есть четкое разделение “реализация - интерфейс”.
Аргументов может быть больше двух (не только a, b).
Использованы минимум три паттерна проектирования “Декоратор”, “Фабричный метод”, “Одиночка”. “Декоратор” дополняет “Фабричный метод”. “Одиночка” используется для реализации простейшего логгера и может быть использован в связке со “Стратегией”. Например, пишем логи в консоль, если файл лога содержит более пяти строк (как показательное решение), то вывод в консоль.
* При реализации обратите внимание, что калькуляторов может быть в будущем несколько, например, обычный, научный, инженерный и т.д.






"""

import calc as cl



var = cl.SimpleCalculator(10, -5, 4,6,2,-6,7,7)
a,b,cifr = var.declare()
print(f"peremennix :\n\t\ta = {a}\n\t\tb = {b}\n\t\tnumbers = {cifr}")
# operator  + 
print(f"slojenie cifr raven :  {var.get('+')}")
# operator  - 
print(f"vichitanie cifr raven :  {var.get('-')}")
# operator  * 
print(f"umnojenie a*b raven :  {var.get('*')}")
# operator  / 
print(f"delenie a/b raven :  {var.get('/')}")
# operator vozvedenie v stepen  **
print(f"vozvedenie v stepen a^b raven :  {var.get('-')}")
# operator  % 
print(f"ostatok ot delenie a%b raven :  {var.get('%')}")
# operator  // 
print(f"celochislennoe delenie raven :  {var.get('-')}")


