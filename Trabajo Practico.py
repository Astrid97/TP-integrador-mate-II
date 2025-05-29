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





    
            
