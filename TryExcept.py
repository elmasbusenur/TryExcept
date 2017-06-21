sayi1=input("SAYİ1:")
sayi2=input("SAYİ2:")
try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1/sayi2)
except ZeroDivisionError:
    print("bir sayi sıfıra bölünemez")
except ValueError:
    print("lütfen bir sayi giriniz")
