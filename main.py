frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)  
#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
elemento-->str-->elemento
Salidas
lista-->list-->lista
"""
def eliminar_un_caracter_de_toda_la_lista(lista:list,elemento:str)->list:
 auxilar=[]
 for i in lista:
   a=i.replace(elemento,"")
   auxilar.append(a)
 return auxilar
if __name__ == "__main__":
  #print(lista_frutas_dos=eliminar_uncaracter_de_toda_la_lista(lista_frutas,"/n")
  lista_frutas_sin_m=eliminar_un_caracter_de_toda_la_lista
  (lista_frutas_dos,"m")
  print(lista_frutas_sin_m)
#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->lista
"""
def copia_lista(lista:list)->list:
  return lista.copy()
if __name__ == "__main__":
  copia=(copia_lista(lista_numeros))
  lista_nueva=eliminar_un_caracter_de_toda_la_lista(copia,"/n")
  print(copia_lista(lista_numeros))


#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->lista
"""  
def numeros_enteros(lista:list):
  auxilar=[]
  auxilar_dos=[]
  for i in lista:
    auxilar.append(float(i))
  for i in auxilar:
    auxilar_dos.append(int(i))
  return auxilar_dos


if __name__ == "__main__":
  copia=(copia_lista(lista_numeros))
  lista_nueva_2=eliminar_un_caracter_de_toda_la_lista(copia,"/n")
  print(numeros_enteros(lista_nueva_2))
  
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
Salidas
"""  
if __name__ == "__main__":
  #print(lista_frutas)
  lista_frutas_dos=elimina_elemento_lista(lista_frutas,"/n")
  lista_frutas_sin_fresa=elimina_elemento_lista(lista_frutas_dos,"kiwi")
print(lista_frutas_sin_kiwi)

#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
Salidas
"""  
def letra(letra:str,lista)->list:
  Auxiliar=[]
  for i in lista:
    if i [0]== letra:
      auxiliar.append(i)
  return(Auxiliar)
  pass  
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
Salidas
"""   
from array import array
numeros=array("i",()
def tamano_lista():
print(len(numeros))
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
Salidas
"""  
def informacion_lista():
  pass
#Retornar una lista con los numero negativos  
"""
Entradas:
Salidas
"""  
def numeros_negativos(lista):
  pass
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
frutas = open('frutas.txt', 'r')
#manejo de exception:FileNotFoundError
try:
  with open(frutas) as f_obj:
    contents=f_obj.read()
    print(contents)
except FileNotFoundError:
  msg="mmm...pareceque el archivo"+frutas+"no existe"
  print(msg)
else:
  #contar las palabras:
  words=contents.split()
  num_words=len(words)
  print("El archivo"+frutas+"contiene:"+str(num_words))
def posicion_elemento(elemento):
  pass
#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(elemento):
  pass
#Realizar una funcion que cuente el numero de veces que se repite un elemento
# "Arándano","Frambuesa","Fresa","Grosella" ,"espinosa","Grosella negra","Grosella","oja","Zarzamora","Limón","Mandarina","Naranja","Pomelo","MelónSandía","Aguacate","Carambola","Chirimoya","Coco","Dátil"-> a,1
from collections import counter
texto="Arándano","Frambuesa","Fresa","Grosella" ,"espinosa","Grosella negra","Grosella","oja","Zarzamora","Limón","Mandarina","Naranja","Pomelo","MelónSandía","Aguacate","Carambola","Chirimoya","Coco","Dátil"
contador=counter(texto)
print(contador)  
