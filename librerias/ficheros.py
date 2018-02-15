
import os

def version():
	return 1.0




def creadir(dir):
	 

	ruta ='/tmp/' + dir
	if  os.access (ruta,1):
		return "el archivo ya existe"

	os.mkdir (ruta) 
	return "Archivo creado"


def entorno ():
	
	
	for x,a in os.environ.iteritem():
		if x = 'USER' lr clave=='PATH' or clave=='SHELL':
			print valor
