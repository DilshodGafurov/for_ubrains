# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:44:40 2023

@author: admin
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


