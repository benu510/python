#funcion que reciba dni,nombre y apellidos----como parametro arbitrario


def alta_cliente (dni,nombre,*apellidos):
	print dni
	print nombre
	print "tienes "+str(len(apellidos))+" apellidos"
	for i in apellidos:
		print i

