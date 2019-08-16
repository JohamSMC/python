course = "Curso"
my_string = 'Codigo Facilito'

#Formas de contatenar mensajes 

final_menssage= 'El nuevo '  + course + " es de " + my_string
final_menssage= "El nuevo %s es de %s " %(course,my_string)
final_menssage= "El nuevo {} es de {} ".format(course,my_string)

final_menssage2= "El nuevo {a} es de {b}".format(b=course,a=my_string)

print (final_menssage)
print (final_menssage2)

"""Metdos de Formato"""
print()
print (final_menssage2.lower())  #Metodo lower() pasa a minuscula todo el String
print (final_menssage2.upper())  #Metodo upper() pasa a Mayuscula todo el String
print (final_menssage2.title())  #Metodo title() pasa a la primera letra de cada palabra a Mayuscula del String

"""Busqueda"""
print()
print(final_menssage2.find('es')) #El metodo find() devuelve la posicion donde comienza el texto enviado por parametro
print(final_menssage2[25:27])

print()
print(final_menssage2.count('e')) #El metodo count() devuelve el numero de veces que esta el texto en la cadena

print()
print(final_menssage2.replace('e','X')) #El metodo replace remplaza el primer valor[e], por el segundo[X] en una cadena

print()
new_string= "Separa Cada palabra".split(' ') #El metodo split() separa por el parametro y devuelve una LISTA
print(new_string)

print()
new_string2="Primera Linea\nSegunda Linea\nTercera Linea".splitlines()
print(new_string2)

print()
print("""1 Linea
	2 Linea
	3 Linea""".splitlines())
