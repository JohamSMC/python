my_list=["string", 15 , 20.3 ,True]	
 
my_list.append("Al final")  #El metodo Appeend() añade un elemeto al final de la lista

my_list.insert(1,"insert posicion 1")  #El metodo Insert() permite añadir un elemento a uan lista especificando el índice

my_list.remove(15) 			#El metodo Remove(), elimina el elemento que se envia como parametro

last_value=my_list.pop() 				#El metodo Pop(), elimina el ultimo elemento de la lista

print(last_value)
print(my_list)