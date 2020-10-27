#mientras el número de carateres ingresados para un usuario de Instagram sea más de 8, se pedirá que vuelva a ingresarse. 
nombre = input("ingrese el nombre de usuario")
def nombreinsta(nombre): 
    while len(nombre)>8:#que se repitan hasta que el nombre sea menor a los caracteres que definas en los parametros
      nombre = input("ingrese el nombre de usuario otra vez")
    return nombre
 
	
#TikTok asigna el espacio de alcenamiento a partir de la edad del usuario
def tiktok(edad):
    resultado=pow(edad,2)
    return resultado

edad=int(input("TikTok asigna como espacio de almacenamiento en GB calculando la edad del usuario elevada al cuadrado,dime tu edad:"))
print("tiktok da", tiktok(edad))


#Devuelve "valido" si la contraseña de TikTok ingresada son todos digitos, en caso contrario retorna "Ingrese solo números"
def tiktok(contra):
  correcto="valido"
  incorrecto="incorrecto"
  if (str.isdigit(contra)):
    return correcto
  else:
    return incorrecto



#Dado el nombre de un canal de Youtube coloca  la primer letra en mayúscula
def analizar(a):
    return (a).capitalize()
    
#Devuelve T si la contraseña de TikTok ingresada son todos digitos, en caso contrario retorna F
def contraseñatt(a):
    if str.isdigit(a)==True:
        return ("T")
    else:
        return ("F")


#mi funcion se trata de que el usuario ingrese un nombre para instagram, lo unico que el nombre que ingresen debe contener menos de 8 letras, si tiene mas el programa le idicara al usuario que es invalido.
print("(tu nombre debe contener menos de 8 letras)")
print("")
def nombreUsuario (nombre):
	letras= len(nombre)
	if letras<8:
	    mensaje= "ok", nombre
	else:
	    mensaje= "es invalido"
	return mensaje
  
	
#Devuelve True si la contraseña de TikTok ingresada son todos digitos, en caso contrario retorna False
def verificacion(num1):
	num1 =str.isdigit(num1)
	if (num1):
		print("tu contraseña es valida")
	else:
		print("tu contraseña no es valida, profavor inglese solo numeros")
	return(num1)


#Retorna True si la contraseña para TikTok son todos números o False en caso contrario
contraseña = input("ingrese su contraseña de tiktok, ingrese unicamente numeros")
verificador = 0
def clavedetiktok (parametro,parametro1):
    parametro = str.isdigit(parametro1)
    if (parametro) :
        print("se guardo tu contraseña en tu usuario de tiktok")
    else :
        print("tu contraseña contiene letras, coloque unicamente numeros en su contraseña")
    return parametro
