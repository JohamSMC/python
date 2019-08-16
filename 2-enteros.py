from math import ceil, floor

number_One =10
number_Two =4

print ("Primer numero: ",number_One)
print ("Segundo numero:",number_One,"\n")
print ("La Suma es: ",number_One+number_Two)
print ("La Resta es: ",number_One-number_Two)
print ("La Multiplicación es: ",number_Two*number_One)

#Devuelve es flotante
print ("La Division es: ",number_One/number_Two ,)

#Devuelve un entero(//)
print ("La Division '//'es: ",number_One//number_Two)

#Regreso un numero a su exponencial(**)
print ("El exponencial '**' es: ",(number_One**number_Two))

"""Redondear al entero anterior o posterior: las funciones floor() y ceil()"""

print ("\nValor sin Redondear")
print(5/2)
print ("Redondear al entero anterior")
print(floor(5/2))
print ("Redondear al entero posterior")
print(ceil(5/2))

print ("\nRedondear valor con un numero de cifras especifico")
print("{0:.3f}".format(5.11299))
print("{0:.4f}".format(5.11299))
