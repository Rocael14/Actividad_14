def menu():
    print("---MENU---")
    print("1. Agregar Participante")
    print("2. Mostrar participantes ordenados por nombre")
    print("3. Mostrar participantes ordenados por edad")
    print("4. Salir")

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1]["paquetes"] < pivote[1]["paquetes"]]
    iguales = [x for x in lista if x[1]["paquetes"] == pivote[1]["paquetes"]]
    mayores = [x for x in lista[1:] if x[1]["paquetes"] > pivote[1]["paquetes"]]

    return quick_sort(mayores) + iguales + quick_sort(menores)

participantes = {}
while True:
    menu()
    try:
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                print("Agregar Participante")
                cantidad_participantes = int(input("Cuantos Participantes desea agregar? : "))
                for i in range(cantidad_participantes):
                    dorsal = int(input(f"Ingrese el dorsal del participante #{i+1}: "))
                    if dorsal >= 0:
                        nombre = input(f"Ingrese el nombre del participante #{i+1}: ")
                        edad = int(input(f"Ingrese el edad del participante #{i+1}: "))
                        while True:
                            seleccion_categoria = int(input(f"Seleccione la categoria del participante #{i+1}: (1. JUVENIL, 2. ADULTO O 3. MASTER)"))
                            if seleccion_categoria == 1:
                                categoria = "JUVENIL"
                                break
                            elif seleccion_categoria == 2:
                                categoria = "ADULTO"
                                break
                            elif seleccion_categoria == 3:
                                categoria = "MASTER"
                                break
                            else:
                                print("Seleccione una categoria valida")
                        participantes[dorsal] = {"nombre":nombre, "edad":edad, "categoria":categoria }

            case 2:
                print("Mostrar Participantes ordenados por nombre")
                lista_participantes_nombre = list(participantes.values())
                ordenamien
                for dorsal, dato in lista_participantes_nombre:
                    print(f"{dorsal}: {dato['nombre']} ({dato['categoria']}))")
            case 3:
                print("Mostrar Participantes ordenados por edad")
            case 4:
                print("Gracias por utilizar el programa")
            case _:
                print("Opcion invalida")
    except Exception:
        print("Solo es permitido ingresos numericos")