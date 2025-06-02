# Desarrollo del programa mediante funciones

dnis = [43307622,41854035,37057172,37378875,38252054]  

# Eliminar los digitos duplicados de cada elemento de la lista
# Ordenar el resultado de menor a mayor


def descomponer_dni(dni):
    
    digitos = []
    
    # Manejo del caso especial 0
    if dni == 0:
        return [0]
    
    # Extracción de dígitos de derecha a izquierda
    while dni > 0:
        digito = dni % 10  # Obtiene el último dígito
        digitos.append(digito)
        dni = dni // 10    # Elimina el último dígito
    # Los dígitos se obtuvieron en orden inverso, así que invertimos la lista
    digitos.reverse()

    return digitos


def digitos_unicos(digitos):
    # Inicializamos una lista de 10 posiciones en false
    encontrados = [False] * 10 #[false,false,false,false,false,false,false,false,false,false]
    unicos = []
    
    for d in digitos: #recorremos digito a digito ("d" es cada elemento de la lista)
        if not encontrados[d]: # si la posición del digito que estamos evaluando ("d") se encuentra en false
            unicos.append(d) # lo agrego a la lista
            encontrados[d] = True  #actualizo la posicion a true
    
    return unicos

def ordenar_counting(dig_uni):   
    # Creo una lista de diez posiciones en 0
    conteo = [0] * 10
    
    # recorrecomos a la lista de digitos unicos, teniendo en cuenta que tiene que incluir valores de 0 a 9
    for d in dig_uni:
        if d == 0:
            conteo[0] = 10 # utilizamos el 10 como referencia a 0 (si es que existe)
        else:
            conteo[d] = d # en la posición de la lista conteo, guardamos el valor del digito
    
    #Reconstruimos la lista ordenada
    ordenados = []
    for c in conteo:  # Recorremos la lista de posiciones existentes
        if c == 10:  # Si el valor en la posicion es igual a 10, sabemos que es 0 y lo reemplazamos
            ordenados.append(str(0))
        elif c > 0 : #mientras los valores siguientes no sean 0, lo agregamos
            ordenados.append(str(c))
    return "{" + ", ".join(ordenados) + "}"



def recorrer_dnis(dnis):
    print(f"Todos los dni {dnis}")
    con = 1
    for dni in dnis:
        digitos = descomponer_dni(dni)
        print(f"DNI {con}: {dni}")
        print(f"Dígitos: {digitos}")
        dig_uni = digitos_unicos(digitos)
        print(f"Digitos unicos: {dig_uni}")
        ord = ordenar_counting(dig_uni)
        print(f"Ordenado: {ord} \n")
        con += 1
    return ord

fun = recorrer_dnis(dnis)



#Estadisticas sobre DNIs y control de flujo
#Recorriendo DNIs y contando la frecuencia de digitos por DNI
DNIs = [43307622, 41854035, 37057172, 37378875, 38252054]

for dni in DNIs:
    print(f"Analizando DNI: {dni}")

#Diccionario {} y for para saber la cantidad de numeros x que tiene un DNI. Por ejemplo tiene dos numeros: dos
    frecuenciaDigitos = {}

    for digito in str(dni):
        if digito in frecuenciaDigitos:
            frecuenciaDigitos[digito] += 1
        else:
            frecuenciaDigitos[digito] = 1

    print (f"Frecuencia de digitos en {dni}: {frecuenciaDigitos}")

#Suma digitos de cada DNI
    suma = 0
    for digito in str(dni):
        suma += int(digito)

    print(f"Suma total de digitos en {dni}: {suma}")

#Diversidad numerica alta
    digitosUnicos = []

    for digito in str(dni):
        if digito not in digitosUnicos:
            digitosUnicos.append(digito)

    if len(digitosUnicos) >= 6:
        print("Diversidad numerica alta")
    else:
        print("Diversidad numerica normal")

#años de nacimiento y logica bisiesta
#Pregunto cuantos usuarios son y recolecto sus años de nacimiento en una lista

Lista_años = [1999, 1997,1992,1993,1994]
lista_edades = []
producto_cartesiano = []

# Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
impares = 0
pares = 0
for año in Lista_años: 
    if año % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Nacieron en años pares {pares} personas\nNacieron en años impares {impares} personas.")

#Si todos nacieron después del 2000, mostrar "Grupo Z".
Grupo_Z = 0

for año in Lista_años:
    if año < 2000:
        Grupo_Z += 1

if Grupo_Z == 0:
    print("Grupo Z")
        
#Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
#Implementar una función para determinar si un año es bisiesto.
def es_bisiesto (año):
    esMultiplode4 = año % 4 == 0
    esMultiplode100 = año % 100 == 0
    esMultiplode400 = año % 400 == 0
    esExcepcion = esMultiplode100 and not esMultiplode400
    
    if esMultiplode4 and not esExcepcion:
        return True
    else:
        return False

Especial = 0
for año in Lista_años:
    bisiesto = es_bisiesto(año)
    if bisiesto == True:
        Especial += 1 

if Especial > 0 :
    print("Tenemos un año especial")
    
        
# Cálculo de edades y producto cartesiano
for año in Lista_años:
    año_actual = 2025

    if (año < año_actual):
        lista_edades.append(año_actual - año)
    else:
        "El año de nacimiento no puede ser mayor a año actual"


for año in Lista_años:
    for edad in lista_edades:
        producto_cartesiano.append([año, edad])

print(f"El producto cartesiano de lista_años = {Lista_años} y lista_edades = {lista_edades} es: {producto_cartesiano}")


#Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica

def union(A, C):
    return A | C

def interseccion(A, C):
    return A & C

def diferencia(A, C):
    return A - C

def diferencia_simetrica(A, C):
    return A ^ C

def operaciones_conjuntos(A, C): #Realiza operaciones de conjuntos entre A y C
    
    
    return {
        'Conjunto A': A,
        'Conjunto C': C,
        'Unión (A | C)': union(A,C),
        'Intersección (A & C)': interseccion(A,C),
        'Diferencia (A - C)': diferencia(A,C),
        'Diferencia (C - A)': diferencia(C,A),
        'Diferencia simétrica (A ^ C)': diferencia_simetrica(A,C)
    }

A = {4,3,3,0,7,6,2,2} # Utilizamos el dni en la posición [0] de la lista como conjunto
C = {3,7,0,5,7,1,7,2} # lo mismo, pero con la posicion [2]

resultados = operaciones_conjuntos(A, C)

print("Resultados para:")
print(f"A = {A} ")
print(f"C = {C} \n")

print("Operaciones con conjuntos:")
for operacion, resultado in resultados.items():
    print(f"{operacion}: {resultado}")


    
 #“Si la intersección entre conjuntos contiene más de 3 elementos, se considera que es una intersección con
 # alta diversidad numérica” 

def alta_diversidad_numerica(c1, c2):
    inter = interseccion(c1,c2)
    return len(inter) > 3  #si la interseccion tiene mas de 3 elementos, devuelve true. Caso contrario, devuelve false


#“Si la diferencia entre dos conjuntos (por ejemplo, A - B) tiene la misma cantidad de elementos que el primer 
# conjunto (A), entonces no había elementos comunes entre los dos conjuntos iniciales”          

def conjuntos_disjuntos(c1, c2):

    dif = diferencia(c1,c2)
    return len(dif) == len(c1) # devuelve true si son disjuntos, y false si tienen elementos en comun

print(f"A  = {A} /n C  = {C} /n")
print(f"¿A y C tienen alta diversidad numérica?: {alta_diversidad_numerica(A, C)}")
print(f"¿A y C son disjuntos?: {conjuntos_disjuntos(A, C)}")