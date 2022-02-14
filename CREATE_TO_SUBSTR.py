import re
datos = ''
with open("datos.txt") as fname:
    lineas = fname.readlines()
    n1=1
    n2=0
    b= False
    for linea in lineas:
        datos=re.findall(r'[(](.*?)[)]', linea)
        linea=str(datos[0])
        print(datos[0])
        linea=linea.replace('VARCHAR2','')
        linea=linea.replace('NUMBER','')
        linea=linea.replace('\t','')
        linea=linea.strip('\n''abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ,() ')
        
        if ',' in datos[0]:
            linea=linea.split(',')
            n1=int(linea[0])+n1#n1 es el contador
            n2=int(linea[0])#n2 va a hacer referencia a la cantidad de posiciones a recoger    
        else:
            n1=int(linea)+n1
            n2=int(linea)

        #pasamos al txt
        f = open('posiciones_ctl.txt','a')
        if b==False:
            b=True
            f.write('SUBSTR (1')
        f.write(','+str(n2)+')')
        #print(n1)
        f.write('\n' + 'SUBSTR (' + str(n1))
        f.close()
        


