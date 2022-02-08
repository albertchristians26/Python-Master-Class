#enumerate
kata = 'abcdefghij'
for item in enumerate(kata):
    print(item)

#unpack tuple in enumerate'
a = []
b = []
print(type(b))
for a,b in enumerate(kata):
    print(a,b)

print(type(b))

#ZIP
list1 = [1,2,3,4,5,]
list2 = ['a','b','c','d','e']

for item in zip(list1, list2):
    print(item)
print(list(zip(list1,list2)))

#Item Checking
box = 'aku belajar'
print('v' in box)

kotak1 = {'a':100,'b':200}
print('a' in kotak1)

print(200 in kotak1.values())

#loop advanced
isi = list(range(1,11))
print(isi)

isi2 = [item**2 for item in range(1,11)]
print(isi2)

even = [item for item in range(1,11) if item%2==0]
print(even)

even = [item if item%2==0 else 'angka ini ganjil' for item in range(1,11) ]
print(even)