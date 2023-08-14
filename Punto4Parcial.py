# Cree una función que reciba un string s1 y retorne la posición de la última ocurrencia del caracter c si está en s1. Si no está, retorne -1 usando dividir y vencer..
#caso_pruebax = (s1,c)
# caso_prueba1 = ("oh","o") #retorno correcto: 0
# caso_prueba2 = ("xxyyyyxxxxxyyyyx","x") #retorno correcto: 15
# caso_prueba3 = ("jfjf","x") #retorno correcto: -1
# caso_prueba4 = ("Holamundo","l") #retorno correcto: 2
def funcion4(s1, c):
    if len(s1) == 0:
        return -1
    
    if len(s1) == 1:
        if s1[0] == c:
            return 0
        else:
            return -1

    mitad = len(s1) // 2
    pos_en_mitad = funcion4(s1[mitad:], c)

    if pos_en_mitad == -1:
        return funcion4(s1[:mitad], c)
    else:
        return mitad + pos_en_mitad

# Casos de prueba
print(funcion4("oh", "o"))
print(funcion4("xxyyyyxxxxxyyyyx", "x"))  
print(funcion4("jfjf", "x"))  
print(funcion4("Holamundo", "l"))  

