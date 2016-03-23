
def dodawanie(a,b):
	return a+b
def get_info():
	return "TO jest program kalkulator"
	

try:
	a = int(input("podaj pierwsza liczbe"))	
	b = int(input("podaj pierwsza liczbe"))	
	print(dodawanie(a,b))	
except ValueError as ve:
	print("wprowadzono bledne dane, koncze dzialanie..")	
	
print(get_info())	
input()
