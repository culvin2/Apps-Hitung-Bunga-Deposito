print("---------Deposito---------")
print("-------Bunga 6.25%--------")

def Bunga_Bank (a,b):
    aa = ((6.25/100)/12)
    c = a * aa
    hasil = a + c
    if b ==1:
        return int(hasil)
    else:
        return int(c+ Bunga_Bank(a,b-1))
print("---Jangka Waktu 1 Tahun---")
a = int(input("Masukkan saldo awal     : " ))
b = int(input("Masukkan bulan ke (1-12): "))
print(Bunga_Bank(a,b))

