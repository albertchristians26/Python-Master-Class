# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 11:51:09 2022

@author: ALBERT
"""

#TUPLES IMMUTABLE

keranjangt = (1,2,3,4,5)
keranjangt2 = 1,2,3,4,5

print(type(keranjangt))

#cara mengindeks tuple sama dengan list

#cara merubah nilai sebuah tuple reassignment
keranjangt = list(keranjangt)
keranjangt[3]='jeruk'
keranjangt = tuple(keranjangt)

#method tuple
t1 = (1,2,3,4,5,6,2,2,2,2)
print(t1.count(2))

print(t1.index(5))

#multiple assignment
a,b,c,d = 1,2,3,4

i = j = k = l = 10

x, y = 8, 9

x, y = y, x

tas = ('sayur', 2, 3.5, [1,2,3,4])
item1, item2, item3, item4 = tas


#SETS
set1 = set()
set1.add('biru')
set1.add('kuning')

list_angka = [1,2,3,3,3,3,3,4,4,5,7,9]
set_angkat = set(list_angka)
print(set_angkat)