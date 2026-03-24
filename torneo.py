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
                equipo = input("Agregar equipo: \n").strip().title()

                if equipo == "":
                    print("Nombre vacío")

                elif equipo in equipos:
                    print("El equipo ya existe")

                elif not all(c.isalpha() or c == " " for c in equipo):
                    print("---Ingrese sólo letras y espacios---")

                else:
                    equipos[equipo.title()] = 0
                    print("Equipo agregado")
                    break

        case "2":
            print("Registrar resultado")

            local = input("Ingresar nombre de equipo local: ").strip().title()
            visitante = input("Ingresar nombre de equipo visitante: ").strip().title()

            if local not in equipos or visitante not in equipos:
                print("Uno o ambos equipos no existen")

            else:
                while True:
                    marcador = input("Ingresar: goles local - goles visitante (ej: 4-2): ").strip()

                    partes = marcador.split("-")

                    if len(partes) != 2:
                        print("Formato inválido")
                        continue

                    g1 = partes[0].strip()
                    g2 = partes[1].strip()

                    if not g1.isdigit() or not g2.isdigit():
                        print("Debe ingresar números positivos 0 o más")
                        continue

                    goles_local = int(g1)
                    goles_visitante = int(g2)

                    if goles_local > goles_visitante:
                        equipos[local] += 3

                    elif goles_local < goles_visitante:
                        equipos[visitante] += 3
   
                    else:
                        equipos[local] += 1
                        equipos[visitante] += 1

                    print("\n Resultado registrado")

                    break
                
        case "3":
            if not equipos:
                print ("La tabla está vacía \n")
            else:
                print("----Esta es la tabla de posiciones: ----\n")

                tabla_ordenada = sorted(equipos.items(), key=lambda x: x[1], reverse=True)

                for equipo, puntos in tabla_ordenada:
                    print(f"{equipo}: {puntos} puntos")

        case "4":
            equipoE = input("Ingresar nombre de equipo a eliminar \n").strip().title()
            
            if equipoE in equipos:
                del equipos[equipoE]
                print(f"Equipo {equipoE} eliminado")
            else:
                print("El equipo no existe")
                
        case "5":
            print("Saliendo ...")
            break

        case _:
            print("Opción inválida")
