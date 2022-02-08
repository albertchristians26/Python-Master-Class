# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 11:38:17 2022

@author: ALBERT
"""

#Contoh Dictionary

dict1 = {'k1' : 'ayam', 'k2' : 'kambing', 'k3' : 'sapi'}

print(dict1['k2'])

daftar_harga = {'kijang innova':250, 'avanza':200, 'vios' :220}
print(daftar_harga['avanza'])

dict2 = {'k1' : 'ayam', 'k2':30,'k3':['a','b',20.5],'k4':{'k5':'apel','k6':'jeruk','k7':'pisang'}}

print(dict2['k4']['k6'])

dict2['k3'] = 'ganti item'

#function dictionary
print(dict2.keys())
print(dict2.values())
print(dict2.items())

print(dict2['k4']['k6'].upper())