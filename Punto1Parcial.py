
# E1. Cree una función que dado un string alfabético con minúsculas y mayúsculas devuelva un string con todas las minúsculas a la izquierda y todas las mayúsculas a la derecha usando dividir y vencer

# caso_prueba1 = "aEiOUUUUffffff" #retorno correcto: aiffffffEOUUUU
# caso_prueba2 = "OOOOOooooo" #retorno correcto: oooooOOOOO
# caso_prueba3 = "" #retorno correcto: ""
# caso_prueba4 = "Holamundo" #retorno correcto: "olamundoH"
def funcion1(cadena):
    if len(cadena) <= 1:
        return cadena
    mid = len(cadena) // 2

    parte_izquierda = funcion1(cadena[:mid])
    parte_derecha= funcion1(cadena[mid:])

    if parte_izquierda[-1].islower() and parte_derecha[0].isupper():
        return parte_izquierda + parte_derecha
    else:
        return parte_derecha + parte_izquierda



caso_prueba1 = "aEiOUUUUffffff"
caso_prueba2 = "OOOOOooooo"
caso_prueba3 = ""
caso_prueba4 = "Holamundo"

print(funcion1(caso_prueba1))  
print(funcion1(caso_prueba2)) 
print(funcion1(caso_prueba3))  
print(funcion1(caso_prueba4)) 




    