guiatelefonica = {}

print("Ingresar 1 para agregar contacto")
print("Ingresar 2 para buscar contacto")
   
def agregarcontacto():
    global guiatelefonica
    nombre = input("Ingrese nombre de contacto: ")
    numero = int(input("Ingrese número de contacto: "))
    guiatelefonica['Guía Telefónica'] = nombre, numero
    print(guiatelefonica)

def buscarcontacto():
   buscar = input("Introduzca el nombre de contacto: ")
   print(guiatelefonica.get(buscar, "No se encontraron resultados"))

option = int(input("Selecciona una opción: "))
if option == 1:
    agregarcontacto()
elif option == 2:
    buscarcontacto()
             