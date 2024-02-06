ilosc_elementow = int(input("Ile elementow chcesz wyslac ?"))
waga = 0
ilosc_paczek = 0


for element in range(ilosc_elementow):
    waga_elementu = float(input("Podaj wage elementu"))
    if waga_elementu >= 1 and waga_elementu <= 10: #Jest to troche bez sensu bo mozemy przecież wysłać 1 element, ktory ma 20 kg i co za tym idzie mieści się w 1 paczce.
        waga = waga + waga_elementu
        ilosc_paczek = 1
        if waga > 20:
            ilosc_paczek += 1
        else: continue
    else:
        print("Waga elementu jest zbyt duża lub zbyt mała proces zostanie przerwany a dotychczasowe POPRAWNIE NADANE paczki wyslane")
        break

suma_pustych_kilogramow = ilosc_paczek * 20 - waga

print(f'Wyslano {ilosc_paczek} paczke/paczki \n Wyslano {waga} kg \n Suma pustych kilogramow: {suma_pustych_kilogramow}') 
if ilosc_paczek > 1:
    print(f'Najwiecej pustych kilogramow ma paczka nr {ilosc_paczek}, {20 - suma_pustych_kilogramow} kg')
else: 
    print(f'Najwiecej pustych kilogramow ma paczka nr {ilosc_paczek}, {20 - waga} kg')







