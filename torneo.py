equipos={}

while True:
    print("\n--- TORNEO ---")
    print("1. Agregar equipo")
    print("2. Registrar resultado")
    print("3. Mostrar tabla")
    print("4. Eliminar equipo")
    print("5. Salir")

    opcion = input("Elegí una opción: ")

    match opcion:
        case "1":
            while True:
                equipo = input("Agregar equipo: \n").strip()

                if equipo == "":
                    print("Nombre vacío")

                elif equipo in equipos:
                    print("El equipo ya existe")

                elif not all(c.isalpha() or c == " " for c in equipo):
                    print("---Ingrese sólo letras y espacios---")

                else:
                    equipos[equipo] = 0
                    print("Equipo agregado")
                break

            for equipo, puntos in equipos.items():
                print(equipo, puntos)

        case "2":
            print("Ingresar equipos y resultado")

        case "3":
            print("Mostrar tabla")

        case "4":
            print("Eliminar equipo")

        case "5":
            print("Saliendo ...")
            break

        case _:
            print("Opción inválida")
