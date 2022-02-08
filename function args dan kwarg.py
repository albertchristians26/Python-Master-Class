#Function

def cetak_kalimat():
    print('ternyata belajar python itu mudah')

cetak_kalimat()

def perkalian(a,b):
    return a*b

print(perkalian(8,10))

def belajar(nama='python'):
    print('saya sedang belajar '+nama)

belajar()

def deteksi_genap(var1):
    '''
    Ini adalah fungsi untuk mendeteksi ganjil dan genap
    '''
    if var1 % 2 == 0:
        print('Angka ini genap')
    else: 
        print('ganjil nih')
    
deteksi_genap(1237)