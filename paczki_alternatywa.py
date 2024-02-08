ilosc_elementow = int(input("Ile elementow chcesz wyslac ?"))
waga_total = 0
waga_paczki = 0
ilosc_paczek = 1

for element in range(ilosc_elementow):
    waga_elementu = float(input("Podaj wage elementu"))
    if waga_elementu < 1 or waga_elementu > 10:
        print("Element zbyt duzy lub zbyt maly")
        break
    else:
        waga_paczki += waga_elementu
        waga_total += waga_elementu

    if waga_paczki + waga_elementu > 20:
        waga_paczki = waga_elementu
        ilosc_paczek += 1


if waga_total <= 20:
    ilosc_paczek = 1
    waga_paczki = waga_total
suma_pustych_kilogramow = ilosc_paczek * 20 - waga_total
print(f'Wyslano {ilosc_paczek} paczke/paczki')
print(f'Wyslano {waga_total} kg')
print(f'Suma pustych kilogramow: {suma_pustych_kilogramow} kg')
print(f'Najwiecej pustych kilogramow miala paczka nr {ilosc_paczek}, {20 - waga_paczki} kg')

