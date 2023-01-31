# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:09:49 2023

@author: admin
"""

class SimpleCalculator:
    def __init__(self, a,b, *numbers):
        """declare of numbers"""
        self.a = a
        self.b = b
        self.numbers = numbers
    def declare(self):
        "return all variables"
        return self.a,self.b, self.numbers
    
    def get(self, oper):
        self.oper = oper
        
        #operatsiya slojenie
        if self.oper == "+":
            if len(self.numbers) != 0:
                self.summa = sum(self.numbers)
                return self.a + self.b + self.summa
            else:
                return self.a + self.b
            
        #operatsiya vichitaniye
        elif self.oper == '-':
            if len(self.numbers) != 0:
                self.subtr = 0
                for i in self.numbers:
                    self.subtr = self.subtr + i
                return self.a-self.b-self.subtr
            else:
                return self.a - self.b
            
        #operatsiya umnojenie
        elif self.oper == '*':
            return self.a * self.b
        
        #operatsiya vozvedenie v stepen
        elif self.oper == '**':
            return self.a ** self.b
        
        #operatsiya delenie
        elif self.oper == '/':
            return self.a / self.b
        
        #operatsiya celochislennoe delenie
        elif self.oper == '//':
            return self.a // self.b

        #operatsiya ostotok ot delenie
        elif self.oper == '%':
            return self.a % self.b


