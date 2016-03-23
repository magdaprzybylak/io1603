<<<<<<< HEAD
def dodawanie():
	a = int(input("Podaj a"))
	b = int(input("Podaj b"))
	print(a+b)

def get_info():
		return "TO jest program kalkulator"
print(get_info()		
dodawanie()	
=======
def dodawanie(a,b):
	return a+b
try:
	a = int(input("podaj pierwsza liczbe"))	
	b = int(input("podaj pierwsza liczbe"))	
	print(dodawanie(a,b))	
except ValueError as ve:
	print("wprowadzono bledne dane, koncze dzialanie..")
>>>>>>> zmiana_funkcji_dodawania
input()
