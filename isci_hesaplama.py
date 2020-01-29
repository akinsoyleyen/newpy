#Ihtiyacimiz olan: Bir erkek kac kutu hangi urunu yapiyor? 1 gunde
#Ihtiyacimiz olan: Bir bayan kac kutu hangi urunu yapiyor? 1 gunde

from sys import argv #?bunu kullanmkyoruz henuz

yapilacak_kutu_sayisi = int(input('Bugun kac kutu mal yapilacak?'))
limon_Telescopic_bayan = 24

def erkekSayisi():
    erkek_sayisi = yapilacak_kutu_sayisi / 300
    erkek_sayisi = round(erkek_sayisi, 0)
    print('Bugun gereken erkek isci sayisi: ' + str(erkek_sayisi))

def bayan_sayisi(limon_Telescopic_bayan, limon_10kg_bayan, greyfurt_15kg_bayan, nar_4kg_bayan):
    bayan_Telescopic_sayisi = yapilacak_kutu_sayisi / limon_Telescopic_bayan
    bayan_Telescopic_sayisi = round(bayan_Telescopic_sayisi, 0)
    print('Bugun telescopic limon icin gereken bayan isci sayisi:' + str(bayan_Telescopic_sayisi))

erkekSayisi()
bayan_sayisi(limon_Telescopic_bayan,0,0,0)


    