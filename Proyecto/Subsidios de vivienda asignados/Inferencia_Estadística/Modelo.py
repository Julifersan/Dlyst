
import numpy as np

# Convertir número logarítmico a número natural
#valorLogaritmico = 19.635549
#NumeroNatural = np.exp(valorLogaritmico)


# y es la variable dependiente (Valor_Asignado)
ymedia = 17.729168005028484

# x1 es la primera variable independiente (Hogares)
x1media = 8.669303148395036
# Primer coeficiente
B1 = 0.012011364826802182

# x2 es la segunda variable independiente (Año_Asignación)
x2media = 2017.0817608450416
# Segundo coeficiente
B2 = 0.04108479853009964

# x3 es la tercera variable independiente (Código_Departamento)
x3media = 39.0685442518716
# Tercer coeficiente
B3 = 0.0024388018020813063

# x4 es la cuarta variable independiente (Código_Programa)
x4media = 162.94671059378524
# B4 cuarto coeficiente
B4 = -0.025024393298752265


# Intercepto
Bo = -61.26399778442749

def modeloy ():
    varindependiente1 : input('Por favor, ingrese el número de hogares: ')
    try:
        varindependiente1 = int(varindependiente1)
    except:
        print('Por favor, ingrese un número entero')
        return #return sirve para reiniciar la pregunta
    
    varindependiente2 : input('Por favor, ingrese el año de asignación: ')
    try:
        varindependiente2 = int(varindependiente2)
    except:
        print('Por favor, digite un año válido, con 4 carácteres numericos: ')
        return
    
    varindependiente3 = input('Por favor, ingrese el código al cual pertenece el departamento que quiere analizar: \n     ')
    try:
        if varindependiente3 == 