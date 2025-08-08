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
    menores = [x for x in lista[1:] if x[1]["edad"] < pivote[1]["edad"]]
    iguales = [x for x in lista if x[1]["edad"] == pivote[1]["edad"]]
    mayores = [x for x in lista[1:] if x[1]["edad"] > pivote[1]["edad"]]

    return quick_sort(menores) + iguales + quick_sort(mayores)

def quick_sort_nombre(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1]["nombre"] < pivote[1]["nombre"]]
    iguales = [x for x in lista if x[1]["nombre"] == pivote[1]["nombre"]]
    mayores = [x for x in lista[1:] if x[1]["nombre"] > pivote[1]["nombre"]]
    return quick_sort_nombre(menores) + iguales + quick_sort_nombre(mayores)

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
                        if dorsal not in participantes:
                            nombre = input(f"Ingrese el nombre del participante #{i+1}: ")
                            edad = int(input(f"Ingrese el edad del participante #{i+1}: "))
                            while True:
                                seleccion_categoria = int(input(f"Seleccione la categoria del participante #{i+1}: (1. JUVENIL, 2. ADULTO O 3. MASTER) "))
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
                        else:
                            print("El dorsal ya esta registrado")
                    else:
                        print("El dorsal no puede ser menor a 0")

            case 2:
                print("Mostrar Participantes ordenados por nombre")
                lista_participantes_nombre = list(participantes.items())
                ordenamiento = quick_sort_nombre(lista_participantes_nombre)
                for dorsal, dato in ordenamiento:
                    print(f"-{dato['nombre']} (Dorsal: {dorsal}, Edad: {dato['edad']}, Categoria: {dato['categoria']})")
            case 3:
                print("Mostrar Participantes ordenados por edad")
                lista_participantes_edad = list(participantes.items())
                ordenamiento = quick_sort(lista_participantes_edad)
                for dorsal, dato in ordenamiento:
                    print(f"-{dato['nombre']} (Dorsal: {dorsal}, Edad: {dato['edad']}, Categoria: {dato['categoria']})")
            case 4:
                print("Gracias por utilizar el programa")
            case _:
                print("Opcion invalida")
    except Exception:
        print("Solo es permitido ingresos numericos")