

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = dict.fromkeys(banknotes_coins, 0)
dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

print(dict_denominations)

for denomination, amount in sorted(dict_denominations.items()):
    print('Denominate:', denomination, '-- amount:', amount)


'''
Dowolną metodą utwórz słownik, który jako klucz będzie przechowywał
wartość nominału, a jeśli chodzi o wartości słownika, 
to póki co mają być zerowe. Proponuję nazwać ten słownik dict_denominations.
'''