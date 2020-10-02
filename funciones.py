#LEN
print ("la longitud del texto cinco es:",len("cinco"))

#REPLACE
texto="hola".replace("a","1")
print("El texto hola tendrá reemplazada la a por 1", texto)

#isdigit
print("Aplicación de isdigit a H0l4 ch1c0s", str.isdigit("H0l4 ch1c0s"))
print("Aplicación de isdigit a 123456789", str.isdigit("123456789"))

#CAPITALIZE
x="hola"
mayuscula=x.capitalize()
print("Capitalize devuelve",mayuscula)

#Rstrip
print("La frase","hola     ","chicos")
x="hola     ".rstrip()
print("funcion Rstrip que saca caracteres en blanco del final de la frase",x,"chicos")

#Lstrip 
texto="            chicos"
print("La frase","hola",texto)
x=texto.lstrip()
print("funcion Rstrip que saca caracteres en blanco al principio","hola",x)


#FUNCIONES NUMERICAS 

#ROUND
print ("La funcion round devuelve tu nota redondeada:",round (5.8))

#POW
print ("raiz cuadrada de 7  es : ", pow(7,2))

#Abs
saldodeudor=abs(-54)
print ("math.sqrt(100) : ",saldodeudor)

#Float
nota=float(5)
print ("float(5): ",nota)

