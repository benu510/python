
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





#Similar a cp.
def cp(forig,fdest):
	if not os.access(forig,0):
		print 'No existe el orígen.'
		exit()
	if os.access(fdest,0):
		print 'Ya existe destino.'
		exit()
	if not os.path.isfile(forig):
		print 'No es un archivo.'
		exit()
	origen=open(forig,'r')
	destino=open(fdest,'w')
	destino.writelines(origen)
	origen.close()
	destino.close()

