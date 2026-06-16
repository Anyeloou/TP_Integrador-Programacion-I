# TP_Integrador-Programacion-I
Integrantes: Fernando Torres- Francisco Ortiz
-----------------------------------------------------------------------------------------------------------------------------------------
El programa permite gestionar información de países desde la consola, a partir de un archivo csv en el cual se guardara la información de cada país. Al ejecutarlo se muestra un meno con 7 opciones, las cuales tienen las siguientes funcionalidades. 
-Agregar país: solicitando datos desde la consola, validando los datos y agregando al csv.
-Actualización de datos: Busca un país por nombre y actualiza los datos de población y superficie. 
-Búsqueda de país: búsqueda de país ingresando nombre completo o parcial por consola, arroja los resultados que coincidan.
-Filtrar países: filtra el dataset por continente, rango de población o superficie, muestra los países encontrados. 
-Ordenar países: ordena el listado por nombre, población o superficie, permitiendo elegir entre manera ascendente como descendente. 
-Ver estadísticas: muestra el país con mayor y menor población, promedio de población y superficie, cantidad de países por continente. 
Todas las opciones tienen validación de entrada y manejo de errores, mostrando claramente en cada caso cual fue el inconveniente o dato incorrecto en caso de que existan. 
--------------------------------------------------------------------------------------------------------------
Requisitos:

-Python 3.10 o superior (se utiliza match/case).
-No requiere bibliotecas externas, solo csv y sys que vienen incluidas en Python.

Estructura del proyecto:
TP_Integrador-Programacion-I/
├── paises.py
└── dataset/
    └── paises.csv

-Ejecutar países.py

-Al iniciar el programa se muestra el menú con las opciones disponibles. Se ingresa el número correspondiente y se presiona Enter:
1-Agregar pais.
2-Actualizar datos(Poblacion y superficie).
3-Buscar pais.
4-Filtrar paises.
5-Ordenar paises.
6-Ver estadisticas.
7-Salir.

-El archivo paises.csv debe estar ubicado en la carpeta dataset y respetar el siguiente formato:
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América

•nombre: texto, no puede ser un número.
•poblacion: número entero positivo.
•superficie: número entero positivo (en km²).
•continente: texto, no puede ser un número.
--------------------------------------------------------------------------------------------------------------
Ejemplos de entradas/salidas esperadas: 

•Buscar país (coincidencia parcial o exacta):

Ingresa opcion: 3

--- Buscar país ---
Ingrese nombre a buscar: ar

Resultados:
Nombre: Argentina | Población: 45376763 personas | Superficie: 2780400km2 | Continente: América

•Filtrar por rango de población:

Ingresa opcion: 4

--- Filtrar países ---
1 - Por continente
2 - Por rango de población
3 - Por rango de superficie
Seleccione una opción: 2

Población mínima: 50000000
Población máxima: 150000000

Se encontraron 2 país(es):

Nombre: Alemania | Población: 83149300 | Superficie: 357022 | Continente: Europa
Nombre: Japón | Población: 125800000 | Superficie: 377975 | Continente: Asia

•Ordenar por superficie descendente: 

Ingresa opcion: 5

--- Ordenar países ---
1 - Nombre
2 - Población
3 - Superficie
Seleccione criterio: 3
¿Ascendente (A) o Descendente (D)?: D

Países ordenados:

Nombre: Brasil | Población: 213993437 Personas | Superficie: 8515767 km2 | Continente: América
Nombre: Argentina | Población: 45376763 Personas | Superficie: 2780400 km2 | Continente: América
Nombre: Nigeria | Población: 223804632 Personas | Superficie: 923768 km2 | Continente: África
Nombre: Japón | Población: 125800000 Personas | Superficie: 377975 km2 | Continente: Asia
Nombre: Alemania | Población: 83149300 Personas | Superficie: 357022 km2 | Continente: Europa
------------------------------------------------------------------------------------------------------------
Enlace al video explicativo: https://www.youtube.com/watch?v=yo5gB9nnwUA
Documento PDF subido en el repositorio. 
Integrantes: 

Fernando Torres: Creación del repositorio principal del proyecto, redacción del README. Creación estructura principal del programa,validaciones, funciones: opción(), agregar_pais(),  mostrar_estadisticas(), salir(). 

Francisco Ortiz: Funciones: actualizar_datos(), buscar_pais(), filtar_paises(), ordenar(), redacción del PDF. 
