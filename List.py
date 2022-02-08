# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 10:21:55 2022

@author: ALBERT
"""

keranjang = [1, 2.3, 'apel']

a = len(keranjang)

for i in range(len(keranjang)):
    print(keranjang[i])
    
for i in range(0,3):
    print(keranjang[i])
    
keranjang[2] = 'mangga'

jeruk = ['jeruk']

keranjang = keranjang + jeruk

keranjang.append('pisang')

keranjang = ['mangga', 'a pel', 'pisang', 'anggur']

buah_lagi = ['nanas', 'kiwi', 'semangka']

keranjang = keranjang + buah_lagi

keranjang.append(buah_lagi)

keranjang.pop()

variabel = ['a','burik','78','8.9']

variabel.sort()

#NESTED LIST
nested_list = [1,2,3,4,5,6,[7,8,9]]

new = nested_list[6][2]