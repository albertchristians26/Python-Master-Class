# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:13:39 2022

@author: ALBERT
"""

#For loop
for i in 'saya belajar python':
    print(i, end='')
    
angka = [1,2,3,4,5,6,7,8,9,10]
for isi in angka:
    print(isi)
    
jumlah = 0
for isi in angka :
    jumlah = jumlah + isi
    print('Hasil pnejumlahan pada iturator ke {} adalah {}'.format(isi,jumlah))
    
print('Hasil penjumlahan total adalah', jumlah)

#looping conditionals
for item in 'saya belajar Python':
    if item == 'a':
        print("Kamu sendang ada di huruf a")
        
#for loop dengan tuple dan lust multiple items
box1 = ((1,2),(3,4),(5,6))
for item in box1:
    print(item)
    
for a,b in box1:
    print(a,b)

#teknik unpack
box2 = [[1,2],[3,4],[5,6]]
for a,b in box2:
    print(a,b)
    
#for a,b,c in box2:
#   print(a) tidak bisa harus sama iterator dan jumlah nilainya


#while loop
indeks = 0
while True:
    print('saya berhasil menjalankan while loop')
    indeks += 1
    if indeks ==10:
        break
    
# continue
angka = [1,2,3,4,5,6,7,8,9,10]
for item in angka:
    if item%2 ==0:
        continue
    else:
        print('anda berada di angka ganjil =', item)

for i in 'Saya sudah mulai mahir di Python':
    if i == 'a':
        pass
    else:
        continue