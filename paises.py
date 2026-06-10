#Importacion de bibliotecas:
import sys
import csv

#Funcion para verificar opcion ingresada: 
def opcion():
    #Muestra por pantalla el menu de opciones disponibles:
    print("-----"*10)
    print("\n1-Agregar pais.\n2-Actualizar datos(Poblacion y superficie).\n3-Buscar pais.\n4-Filtrar paises.\n5-Ordenar paises.\n6-Ver estadisticas.\n7-Salir.\n")
    #Mediante un bloque try except valida la opcion ingresada, while True: se utiliza para pedir la opcion hasta que se ingrese correctamente:
    while True:
        try:
            opc=input("Ingresa opcion: ").strip()
            #Verifica que no este vacio:
            if opc == "":
                raise ValueError("El campo no puede estar vacío.")
            #Verfica que la opcion sea un entero:
            if not opc.isdigit():
                raise ValueError("Debe ingresar un numero entero.")
            opc = int(opc)
            #Verifica que el numero este entre el 1 y 7 incluidos:
            if not 1 <= opc <= 7:
                raise ValueError("El número debe estar entre 1 y 7.")
            #Una vez se ingrese la opcion correctamente retorna la misma (opc):
            return opc
        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Error: {e}\n")


#---------------------Funcionalidades------------------------:

#Verifica si un pais ya existe en el CSV comparando por nombre, evitando duplicados:
def pais_existe(nombre):
    try:
        with open("dataset/paises.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            #Recorre cada fila y compara el nombre ingresado con el almacenado (sin distinguir mayusculas):
            for fila in reader:
                if len(fila) > 0 and fila[0].lower() == nombre.lower():
                    return True

    except FileNotFoundError:
        return False

    return False


#Agrega un nuevo pais con todos sus datos al CSV.
#No se permiten campos vacios ni duplicados:
def agregar_pais():
    print("\n--- Agregar nuevo país ---")
    #Solicitud de nombre:
    nombre = input("Nombre del país: ").strip()
    #Solicita el nombre hasta que sea correcto, no puede estar vacio ni ser un numero:
    while nombre == "" or nombre.isdigit():
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            nombre = input("Nombre del país: ").strip()
        else:
            print("No puedes ingresar numeros: ")
            nombre = input("Nombre del país: ").strip()
    #Guarda el nombre con la inicial en mayuscula:
    nombre = nombre.title()
    #Verifica si el pais ya existe antes de continuar:
    if pais_existe(nombre):
        print("Error: el país ya está cargado.")
        return
    #Solicitud de poblacion, se valida que sea un entero positivo con try/except:
    while True:
        try:
            poblacion = int(input("Población: ").strip())
            if poblacion <= 0:
                raise ValueError("Error: la población debe ser un numero entero positivo.")
            break
        except ValueError:
            print("Error: ingresá un número entero válido.")
        except Exception as e:
            print(f"Error: {e}")
    #Solicitud de superficie en km2, misma validacion que poblacion:
    while True:
        try:
            superficie = int(input("Superficie en km²: ").strip())
            if superficie <= 0:
                raise ValueError("Error: la superficie debe ser un numero entero positivo.")
            break
        except ValueError:
            print("Error: ingresá un número entero válido.")
        except Exception as e:
            print(f"Error: {e}")
    #Solicitud de continente, no puede estar vacio ni ser un numero:
    continente = input("Continente: ").strip()
    while continente == "" or continente.isdigit():
        if continente == "":
            print("Error: el continente no puede estar vacío.")
            continente = input("Continente: ").strip()
        else:
            print("No puedes ingresar numeros: ")
            continente = input("Continente: ").strip()

    #Arma el diccionario con los datos ingresados:
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    #Abre el CSV en modo append para agregar el nuevo pais sin borrar los existentes:
    try:
        with open("dataset/paises.csv", "a", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writerow(pais)
        print(f"\nPaís '{nombre}' agregado correctamente.")
    except IOError:
        print("Error: no se pudo escribir en el archivo.")


#Permite actualizar la poblacion y superficie de un pais existente.
#Lee todo el CSV, modifica la fila correspondiente y reescribe el archivo:
def actualizar_datos():
    print("\n--- Actualizar datos ---")
    #Solicitud del nombre del pais a actualizar, no puede estar vacio:
    nombre_buscar = input("Ingrese el nombre del país a actualizar: ").strip().lower()
    while nombre_buscar == "":
        print("Error: no puede estar vacío.")
        nombre_buscar = input("Ingrese el nombre del país a actualizar: ").strip().lower()

    filas = []
    encontrado = False

    try:
        with open("dataset/paises.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            #Saltea el encabezado para no procesarlo como datos:
            next(reader)
            for fila in reader:
                #Omite filas con formato incorrecto:
                if len(fila) < 4:
                    continue
                nombre = fila[0].lower()
                #Si encuentra el pais solicita los nuevos datos:
                if nombre == nombre_buscar:
                    print(f"País encontrado: {fila[0]}")
                    encontrado = True
                    #Solicita nuevos valores con validacion, while True hasta ingresar datos correctos:
                    while True:
                        try:
                            nueva_poblacion = int(input("Nueva población: "))
                            if nueva_poblacion <= 0:
                                raise ValueError("Ingresa poblacion con numeros positivos.")
                            nueva_superficie = int(input("Nueva superficie: "))
                            if nueva_superficie <= 0:
                                raise ValueError("Ingresa superficie con numeros positivos.")
                            break
                        except ValueError:
                            print("Error: valores inválidos.")
                        except Exception as e:
                            print(f"Error: {e}")
                    #Actualiza los valores en la fila:
                    fila[1] = str(nueva_poblacion)
                    fila[2] = str(nueva_superficie)

                filas.append(fila)

        if not encontrado:
            print("País no encontrado.")
            return
        #Reescribe el archivo completo con la fila modificada:
        with open("dataset/paises.csv", "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerows(filas)
        print("Datos actualizados correctamente.")
    except FileNotFoundError:
        print("Error: archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")


#Busca paises por nombre, admite coincidencia parcial o exacta:
def buscar_pais():
    print("\n--- Buscar país ---")
    #Solicitud del termino a buscar, no puede estar vacio:
    termino = input("Ingrese nombre a buscar: ").strip().lower()
    while termino == "":
        print("Error: el campo no puede estar vacío.")
        termino = input("Ingrese nombre a buscar: ").strip().lower()

    encontrados = []

    try:
        with open("dataset/paises.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            #Saltea el encabezado:
            next(reader)
            for fila in reader:
                if len(fila) < 4:
                    continue
                nombre = fila[0].lower()
                #Verifica si el termino ingresado esta contenido en el nombre del pais:
                if termino in nombre:
                    encontrados.append(fila)
        #Muestra los resultados o un mensaje si no se encontro nada:
        if not encontrados:
            print("No se encontraron países.")
        else:
            print("\nResultados:")
            for pais in encontrados:
                print(f"Nombre: {pais[0]} | Población: {pais[1]} personas| Superficie: {pais[2]}km2 | Continente: {pais[3]}")
    except FileNotFoundError:
        print("Error: archivo no encontrado.")


#Filtra paises segun el criterio seleccionado: continente, rango de poblacion o rango de superficie:
def filtar_paises():
    print("\n--- Filtrar países ---")

    print("1 - Por continente")
    print("2 - Por rango de población")
    print("3 - Por rango de superficie")

    opcion = input("Seleccione una opción: ").strip()
    #Verifica que la opcion ingresada sea valida:
    if opcion not in ["1", "2", "3"]:
        print("Error: opción inválida.")
        return

    resultados = []

    try:
        with open("dataset/paises.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            #Saltea el encabezado:
            next(reader)

            if opcion == "1":
                #Solicita el continente con validacion, no puede estar vacio ni ser un numero:
                while True:
                    try:
                        continente_buscar = input("Ingrese continente: ").strip().lower()
                        if continente_buscar == "":
                            raise ValueError("Error: no puede estar vacío.")
                        if continente_buscar.isdigit():
                            raise ValueError("Error: Ingrese letras.")
                        #Recorre el CSV y agrega los paises que coincidan con el continente:
                        for fila in reader:
                            if len(fila) < 4:
                                continue
                            if fila[3].lower() == continente_buscar:
                                resultados.append(fila)
                        break
                    except Exception as e:
                        print(f"Error: {e}")

            elif opcion == "2":
                #Solicita el rango de poblacion con validacion:
                while True:
                    try:
                        min_pob = int(input("Población mínima: "))
                        if min_pob < 0:
                            raise ValueError("Error: Ingresa numeros positivos.")
                        max_pob = int(input("Población máxima: "))
                        if max_pob < 0:
                            raise ValueError("Error: Ingresa numeros positivos.")
                        #Verifica que el minimo no supere al maximo:
                        if min_pob > max_pob:
                            raise ValueError("Error: El minimo no puede superar el maximo.")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                #Filtra los paises cuya poblacion este dentro del rango ingresado:
                for fila in reader:
                    if len(fila) < 4:
                        continue
                    try:
                        poblacion = int(fila[1])
                        if min_pob <= poblacion <= max_pob:
                            resultados.append(fila)
                    except:
                        continue

            elif opcion == "3":
                #Solicita el rango de superficie con validacion, misma logica que poblacion:
                while True:
                    try:
                        min_sup = int(input("Superficie mínima: "))
                        if min_sup < 0:
                            raise ValueError("Error: Ingresa numeros positivos.")
                        max_sup = int(input("Superficie máxima: "))
                        if max_sup < 0:
                            raise ValueError("Error: Ingresa numeros positivos.")
                        if min_sup > max_sup:
                            raise ValueError("Error: El minimo no puede superar el maximo.")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                #Filtra los paises cuya superficie este dentro del rango ingresado:
                for fila in reader:
                    if len(fila) < 4:
                        continue
                    try:
                        superficie = int(fila[2])
                        if min_sup <= superficie <= max_sup:
                            resultados.append(fila)
                    except:
                        continue
        #Muestra los resultados o un mensaje si no se encontro nada:
        if not resultados:
            print("No se encontraron resultados.")
        else:
            print(f"\nSe encontraron {len(resultados)} país(es):\n")
            for pais in resultados:
                print(f"Nombre: {pais[0]} | Población: {pais[1]} | Superficie: {pais[2]} | Continente: {pais[3]}")

    except FileNotFoundError:
        print("Error: archivo no encontrado.")


#Ordena los paises segun el criterio y el orden seleccionado por el usuario:
def ordenar():
    print("\n--- Ordenar países ---")
    print("1 - Nombre\n2 - Población\n3 - Superficie")
    opcion = input("Seleccione criterio: ").strip()
    #Solicita el criterio hasta que sea valido:
    while opcion not in ["1", "2", "3"]:
        print("Error: opción inválida.")
        opcion = input("Seleccione criterio: ").strip()

    orden = input("¿Ascendente (A) o Descendente (D)?: ").strip().lower()
    #Solicita el orden hasta que sea valido:
    while orden not in ["a", "d"]:
        print("Error: opción inválida.")
        orden = input("¿Ascendente (A) o Descendente (D)?: ").strip().lower()

    try:
        with open("dataset/paises.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            #Saltea el encabezado:
            next(reader)
            paises = []
            for fila in reader:
                if len(fila) < 4:
                    continue
                paises.append(fila)

        if not paises:
            print("No hay datos para ordenar.")
            return

        #Ordena segun el criterio seleccionado usando lambda como clave de comparacion:
        if opcion == "1":
            paises.sort(key=lambda x: x[0].lower())
        elif opcion == "2":
            paises.sort(key=lambda x: int(x[1]))
        elif opcion == "3":
            paises.sort(key=lambda x: int(x[2]))

        #Si el orden es descendente invierte la lista ya ordenada:
        if orden == "d":
            paises.reverse()

        print(f"\nPaíses ordenados:\n")
        for pais in paises:
            print(f"Nombre: {pais[0]} | Población: {pais[1]} Personas | Superficie: {pais[2]} km2 | Continente: {pais[3]}")

    except FileNotFoundError:
        print("Error: archivo no encontrado.")
    except ValueError:
        print("Error: datos inválidos en el archivo.")


#Calcula y muestra estadisticas generales del dataset:
#Pais con mayor y menor poblacion, promedios y cantidad de paises por continente:
def mostrar_estadisticas():
    print("\n--- Estadísticas ---")

    try:
        with open("dataset/paises.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            #Saltea el encabezado:
            next(reader)
            paises = []
            for fila in reader:
                if len(fila) < 4:
                    continue
                #Convierte cada fila a diccionario, omite filas con formato incorrecto:
                try:
                    paises.append({
                        "nombre": fila[0],
                        "poblacion": int(fila[1]),
                        "superficie": int(fila[2]),
                        "continente": fila[3]
                    })
                except ValueError:
                    print(f"Error: fila con formato incorrecto, se omite -> {fila}")
                    continue

        if not paises:
            print("No hay datos para mostrar.")
            return

        #Busca el pais con mayor y menor poblacion usando max y min con lambda:
        mayor_pob = max(paises, key=lambda x: x["poblacion"])
        menor_pob = min(paises, key=lambda x: x["poblacion"])

        #Calcula el promedio de poblacion y superficie dividiendo la suma total por la cantidad de paises:
        promedio_pob = sum(p["poblacion"] for p in paises) / len(paises)
        promedio_sup = sum(p["superficie"] for p in paises) / len(paises)

        #Cuenta la cantidad de paises por continente usando un diccionario:
        continentes = {}
        for pais in paises:
            continente = pais["continente"]
            #Si el continente ya existe suma 1, si no lo inicializa en 1:
            if continente in continentes:
                continentes[continente] += 1
            else:
                continentes[continente] = 1

        #Muestra todos los resultados:
        print(f"\nPaís con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,} habitantes)")
        print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,} habitantes)")
        print(f"Promedio de población: {promedio_pob:,.0f} habitantes")
        print(f"Promedio de superficie: {promedio_sup:,.0f} km²")
        print(f"\nCantidad de países por continente:")
        for continente, cantidad in continentes.items():
            print(f"  {continente}: {cantidad} país(es)")

    except FileNotFoundError:
        print("Error: archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")


#Funcion para salir del programa con la biblioteca sys:
def salir():
    print("Hasta luego!")
    sys.exit(0)


#Bucle principal: ejecuta el menu y llama a la funcion correspondiente segun la opcion elegida:
while True:
    opc = opcion()
    #Match case que deriva a cada funcion segun la opcion, hasta que el usuario elija salir():
    match opc:
        case 1:
            agregar_pais()
        case 2:
            actualizar_datos()
        case 3:
            buscar_pais()
        case 4:
            filtar_paises()
        case 5:
            ordenar()
        case 6:
            mostrar_estadisticas()
        case 7:
            salir()