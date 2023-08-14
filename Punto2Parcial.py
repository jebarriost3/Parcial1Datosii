# Cree una función que determine si un string s1 está contenido en un string s2 usando dividir y vencer
#caso_prueba = (s1,s2)
# caso_prueba1 = ("oh","fohx") #retorno correcto: True
# caso_prueba2 = ("xx","xoxkkkkkx") #retorno correcto: False
# caso_prueba3 = ("jfjf","fjfjfjkkkkkkkkkkk") #retorno correcto: True
# caso_prueba4 = ("Holamundo","Holamundo") #retorno correcto: True

#programa:
def funcion2(s1,s2):
    if len(s1) > len(s2):
        return False
    else:
        if s1 == s2:
            return True
        else:
            mitad = len(s2)//2
            if s1 == s2[0:len(s1)]:
                return True
            else:
                if s1 == s2[mitad:len(s1)+mitad]:
                    return True
                else:
                    if s1 == s2[len(s2)-len(s1):len(s2)]:
                        return True
                    else:
                        return funcion2(s1,s2[1:len(s2)-1])

        
#casos de prueba:
caso_prueba1 = ("oh","fohx") #retorno correcto: True
caso_prueba2 = ("xx","xoxkkkkkx") #retorno correcto: False
caso_prueba3 = ("jfjf","fjfjfjkkkkkkkkkkk") #retorno correcto: True
caso_prueba4 = ("Holamundo","Holamundo") #retorno correcto: True
 
print(funcion2(caso_prueba1[0],caso_prueba1[1]))
print(funcion2(caso_prueba2[0],caso_prueba2[1]))
print(funcion2(caso_prueba3[0],caso_prueba3[1]))
print(funcion2(caso_prueba4[0],caso_prueba4[1]))
 