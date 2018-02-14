#por tecladouna letra y en cuantos ficheros aparece la letr

import os
letra=raw_input('dime una letra:')
total=0
x=os.listdir('c:\windows\system32')
for archivo in x:
  if archivo.count(letra) > 0:
    total=total+1
print total
	