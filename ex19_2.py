tablet_adedi = int(input("Evinde kac bilgisayar var?"))
pc_adedi = int(input("Evinde kac pc var?"))

def evde_kac_bilgisayar_var(tablet_adedi,pc_adedi):
    print(f"Evdeki tablet adedi {tablet_adedi}")
    print(f"Evdeki pc adedi: {pc_adedi}")

evde_kac_bilgisayar_var(tablet_adedi,pc_adedi)
print(f"Toplam bilgisayar adedi: \n")
print(tablet_adedi+pc_adedi)
