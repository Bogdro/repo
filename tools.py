def sprawdz(L):
	"""Funkcja sprawdzająca czy składniki L to int lub float oraz czy to lista lub tuple """
	type1 = [tuple, list]
	type2 = [int, float]
	if type(L) not in type1:
		return False
	else:
		for i in L:
			if type(i) not in type2:
				return False
		
	return True
		
print sprawdz([1,2,3])
print sprawdz([1,"b"])
