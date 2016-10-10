import math
def srednia_kwadratowa(liczby):
	for i in range(len(liczby)):
		liczby[i] = float(liczby[i]*liczby[i])
	wynik = sum (liczby)
	wynik = math.sqrt ( wynik / len(liczby))
	return wynik


