import math
import myerror
def srednia_kwadratowa(liczby):
	if type(liczby) != list and type(liczby) != tuple:
		raise myerror.IBeBack()
	for i in range(len(liczby)):
		liczby[i] = float(liczby[i]*liczby[i])
	wynik = sum (liczby)
	wynik = math.sqrt ( wynik / len(liczby))
	return wynik


