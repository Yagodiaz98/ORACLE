print ("+++ 1 ++++")
import re
datos = ''
with open("datos.txt") as fname:
	lineas = fname.readlines()
	n1=1
	n2=0
	b=False
	numbere='	INTEGER EXTERNAL,'
	numberd='	DECIMAL EXTERNAL,'
	varchar='	CHAR,'
	p_final = ''
	n_number = 0
	n_varchar = 0
	for linea in lineas:
		#print(datos)
		#SI ENCUENTRAS VARCHAR HAZ ESTO, SI ES NUMBER BUSCA UNA COMA
		if 'VARCHAR' in linea:
			p_final=varchar
		else:
			datos=re.findall(r'[(](.*?)[)]', linea)
			print(datos[0])
			if ',' in datos[0]:
				p_final=numberd
				n1 = n1+1 #para tener en cuenta las comas de los decimales
			else:
				p_final=numbere
		linea=linea.replace('VARCHAR2','')
		linea=linea.replace('\t','')
		linea=linea.split(',')
		#datos.append(linea[0].strip('\n''VARCHNUMBE,() '))
		n2=linea[0].strip('\n''abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ,() ')
		n1=int(n1)+int(n2)
		#if n1 != 0:
		f = open('posiciones_ctl.txt','a')
		if b==False:
			b=True
			f.write('POSITION	(1')
		f.write(':'+str(n1-1)+')'+p_final)
		#print(n1)
		f.write('\n' + 'POSITION	(' + str(n1))
		f.close()
print ("+++")


#si tiene coma debo contarla como una posicion