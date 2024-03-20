#Kullanıcının girdiği boy ve ağırlık değerlerine göre 
#vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI ?")
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
 
endeks  = kilo/(boy*boy)
 
if endeks <18:
    print("\n zayıf VKİ:{}".format(endeks))
elif endeks >= 18 and endeks <25 :
    print("\n normal VKİ:{}".format(endeks))
elif endeks >= 25 and endeks <30:
    print("\n kilolu VKİ:{}".format(endeks))
elif endeks >= 30 and endeks <35:
    print("\n obez VKİ:{}".format(endeks))
else:
    print("\n ciddi obez VKİ:{}".format(endeks))

  #Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz. 

yeniMaas=0
maas=input("Maaşi Gir : ")
zam=input("Zam Orani(%) : ")
yeniMaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamli Maaş :",yeniMaas)

#Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
sayi3 = int(input("3. Sayı: "))
 
if (sayi1 >= sayi2) and (sayi1 >= sayi3):
   buyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
   buyuk = sayi2
else:
   buyuk = sayi3
 
print(sayi1,",",sayi2,"ve",sayi3,"içinde büyük olan sayı",buyuk)

#Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını 
#kullanıcıdan alınız)

#yazilimkodlama.com
r=int(input("Yarı Çapı Girin: "))
cevre=2*3.14*r
alan=3.14*r*r
print("Çevre: ",cevre)
print("Alan: ",alan)

#Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

metin = input('Metni Girin : \n')
ters=metin[::-1]

print('Girilen metnin tersi = %s' % (ters))
if ters == metin:
    print('Girilen metin palindrom')
else:
    print('Girilen metin palindrom değil.')