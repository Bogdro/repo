from tools import sprawdz
import math
import myerror
def srednia_kwadratowa(liczby):
	"""
	Funkcja liczaca srednia kwadratowa
	
	liczby - list,tuple
	"""
	#if type(liczby) != list and type(liczby) != tuple:
        ##if sprawdz(liczby) == False:
		##raise myerror.IBeBack()
        assert sprawdz(liczby)
	for i in range(len(liczby)):
		liczby[i] = float(liczby[i]*liczby[i])
	wynik = sum (liczby)
	wynik = math.sqrt ( wynik / len(liczby))
	return wynik


