ilosc_elementow = int(input("Ile elementow chcesz wyslac ?"))
waga_total = 0
waga_paczki = 0
ilosc_paczek = 1
waga_najlzejszej_paczki = 20
numer_najlzejszej_paczki = 0
wagi_paczek = {}
for element in range(ilosc_elementow):
    waga_elementu = float(input("Podaj wage elementu"))
    if waga_elementu < 1 or waga_elementu > 10:
        print("Element zbyt duzy lub zbyt maly")
        break
    if waga_paczki + waga_elementu > 20:
        if waga_paczki < waga_najlzejszej_paczki:
            numer_najlzejszej_paczki = ilosc_paczek
            waga_najlzejszej_paczki = waga_paczki
        wagi_paczek.update({ilosc_paczek: waga_paczki})
        waga_paczki = waga_elementu
        waga_total += waga_elementu
        ilosc_paczek += 1
    else:

        waga_paczki += waga_elementu
        waga_total += waga_elementu


    if waga_najlzejszej_paczki == 0:
        waga_najlzejszej_paczki = waga_paczki


wagi_paczek.update({ilosc_paczek: waga_paczki})
suma_pustych_kilogramow = ilosc_paczek * 20 - waga_total


if waga_total <= 20:
    ilosc_paczek = 1
    waga_paczki = waga_total
    waga_najlzejszej_paczki = waga_paczki
    numer_najlzejszej_paczki = 1
if waga_paczki < waga_najlzejszej_paczki:
    waga_najlzejszej_paczki = waga_paczki
    numer_najlzejszej_paczki = ilosc_paczek

print(f'Wyslano {ilosc_paczek} paczke/paczki')
print(f'Wyslano {waga_total} kg')
print(f'Suma pustych kilogramow: {suma_pustych_kilogramow} kg')
print(f'Najwiecej pustych kilogramow miala paczka nr:')

print('Ze zmiennej: ')
print(numer_najlzejszej_paczki, 20 - waga_najlzejszej_paczki, 'kg')
print('Ze slownika: ')
print(f' {min(wagi_paczek, key=wagi_paczek.get)} {20 - min(wagi_paczek.values())} kg')



