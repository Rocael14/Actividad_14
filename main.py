def menu():
    print("---MENU---")
    print("1. Agregar Participante")
    print("2. Mostrar participantes ordenados por nombre")
    print("3. Mostrar participantes ordenados por edad")
    print("4. Salir")


while True:
    menu()
    try:
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                print("Agregar Participante")
            case 2:
                print("Mostrar Participantes")
            case 3:
                print("Mostrar Participantes ordenados por edad")
            case 4:
                print("Gracias por utilizar el programa")
            case _:
                print("Opcion invalida")
    except Exception:
        print("Solo es permitido ingresos numericos")