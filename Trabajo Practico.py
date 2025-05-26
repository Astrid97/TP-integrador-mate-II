#años de nacimiento y logica bisiesta
#Pregunto cuantos usuarios son y recolecto sus años de nacimiento en una lista
usuarios = int(input("¿Los datos de cuantas personas seran ingresados?: "))

Lista_años = []
lista_edades = []
producto_cartesiano = []

for i in range(usuarios):
    año = int(input(f"Ingrese el año {i+1}: "))
    Lista_años.append(año)
              
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

    

    
            
