import sys
import pip

def ValidaMySQL():
	Encontrado=False
	PaquetesInstalados=pip.get_installed_distributions()
	for modulo in PaquetesInstalados:
		Posicion=str(modulo).find('MySQL')
		if Posicion>=0:
			print "Encontrado"
			return True
		
	return False
