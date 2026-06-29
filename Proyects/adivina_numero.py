def mostrar_bienvenida():
    print("\n" + "=" * 54)
    print("       ╔══════════════════════════════════╗")
    print("       ║  ADIVINATOR: PROYECTO TERMINADO  ║")
    print("       ╚══════════════════════════════════╝")
    print("=" * 54)
    print("   ¡Bienvenido! Pon a prueba mi inteligencia.")
    print("   Piensa un número... y yo lo adivinaré.")
    print("=" * 54)


def mostrar_menu():
    print("\n" + "=" * 54)
    print("                 MENÚ PRINCIPAL")
    print("=" * 54)
    print("   1.  Jugar")
    print("   2.  Instrucciones")
    print("   3.  Como funciona el algoritmo?")
    print("   4.  Creditos")
    print("   5.  Salir")
    print("=" * 54)


def mostrar_instrucciones():
    print("\n" + "=" * 54)
    print("                 INSTRUCCIONES")
    print("=" * 54)
    print("")
    print("   1. Selecciona la opcion Jugar en el menu.")
    print("")
    print("   2. Define el rango en el que quieres que")
    print("      yo adivine (por ejemplo: del 1 al 100).")
    print("")
    print("   3. Piensa en un numero dentro de ese rango")
    print("      y no me lo digas.")
    print("")
    print("   4. Yo hare mis intentos. Por cada uno deberas")
    print("      responderme con:")
    print("")
    print("        mayor   -> si tu numero es MAYOR al mio")
    print("        menor   -> si tu numero es MENOR al mio")
    print("        correcto -> si adivine tu numero")
    print("")
    print("   5. Responde con honestidad.")
    print("")
    print("   6. Al final veras cuantos intentos me tomo")
    print("      y una evaluacion de mi desempeno.")
    print("")
    print("=" * 54)
    input("   Presiona Enter para volver al menu...")


def mostrar_algoritmo():
    print("\n" + "=" * 54)
    print("       COMO FUNCIONA EL ALGORITMO?")
    print("=" * 54)
    print("")
    print("   Uso el algoritmo de BUSQUEDA BINARIA.")
    print("")
    print("   En cada intento calculo el punto MEDIO")
    print("   del rango disponible:")
    print("")
    print("       intento = (minimo + maximo) // 2")
    print("")
    print("   Luego, segun tu respuesta:")
    print("")
    print("     Si dices  mayor  -> descarto la mitad")
    print("     inferior y busco solo en la parte alta.")
    print("         minimo = intento + 1")
    print("")
    print("     Si dices  menor  -> descarto la mitad")
    print("     superior y busco solo en la parte baja.")
    print("         maximo = intento - 1")
    print("")
    print("     Si dices  correcto  -> lo logre!")
    print("")
    print("   Por que es eficiente?")
    print("   Con cada intento elimino la MITAD de los")
    print("   numeros posibles.")
    print("")
    print("   Rango 1-100   -> maximo 7 intentos")
    print("   Rango 1-1000  -> maximo 10 intentos")
    print("")
    print("=" * 54)
    input("   Presiona Enter para volver al menu...")


def mostrar_creditos():
    print("\n" + "=" * 54)
    print("                    CREDITOS")
    print("=" * 54)
    print("")
    print("   Proyecto   : El Computador Adivina Tu Numero")
    print("   Estudiante : Ethan Arellano")
    print("   Universidad: UIDE")
    print("   Materia    : Logica de Programacion")
    print("   Periodo    : 2025")
    print("   Lenguaje   : Python 3")
    print("   Algoritmo  : Busqueda Binaria")
    print("")
    print("   ----------------------------------------")
    print("   El conocimiento que no se aplica")
    print("   no tiene ningun valor.")
    print("                         - Anton Chejov")
    print("")
    print("=" * 54)
    input("   Presiona Enter para volver al menu...")


def obtener_rango():
    print("\n   Define el rango de tu numero:")

    while True:
        try:
            minimo = int(input("   Numero MINIMO del rango: "))
            maximo = int(input("   Numero MAXIMO del rango: "))

            if minimo >= maximo:
                print("   El minimo debe ser menor que el maximo.\n")
                continue
            else:
                return minimo, maximo

        except ValueError:
            print("   Ingresa solo numeros enteros.\n")
            continue


def evaluar_desempeno(intentos):
    if intentos == 1:
        calificacion = "LEGENDARIO - Adivine a la primera!"
    elif intentos <= 3:
        calificacion = "EXCELENTE  - Muy pocos intentos."
    elif intentos <= 6:
        calificacion = "BIEN       - Rendimiento normal."
    elif intentos <= 10:
        calificacion = "REGULAR    - Me costo un poco."
    else:
        calificacion = "MEJORABLE  - Pero lo logre!"

    return calificacion


def computador_adivina(minimo, maximo):
    intentos   = 0
    encontrado = False

    print("\n   Ok! Pense un numero entre " + str(minimo) + " y " + str(maximo) + ".")
    print("   Responde: mayor, menor o correcto\n")

    while minimo <= maximo:

        intento  = (minimo + maximo) // 2
        intentos = intentos + 1

        print("   Intento #" + str(intentos) + ": Tu numero es " + str(intento) + "?")
        respuesta = input("   Tu respuesta: ").strip().lower()

        if respuesta == "correcto":
            encontrado = True
            break

        elif respuesta == "mayor":
            minimo = intento + 1
            continue

        elif respuesta == "menor":
            maximo = intento - 1
            continue

        else:
            print("   Escribe mayor, menor o correcto.")
            intentos = intentos - 1
            continue

    return encontrado, intentos


def mostrar_resultado(encontrado, intentos):
    print("\n" + "=" * 54)

    if encontrado:
        calificacion = evaluar_desempeno(intentos)
        print("   Lo logre! Adivine en " + str(intentos) + " intento(s).")
        print("   Evaluacion: " + calificacion)
    else:
        print("   Algo salio mal. Respondiste con honestidad?")

    print("=" * 54)


def preguntar_repetir():
    while True:
        respuesta = input("\n   Quieres jugar otra vez? (si/no): ").strip().lower()

        if respuesta == "si" or respuesta == "s":
            return True
        elif respuesta == "no" or respuesta == "n":
            return False
        else:
            print("   Escribe si o no.")
            continue


def ejecutar_juego():
    partidas = 0

    while True:
        partidas = partidas + 1
        print("\n" + "-" * 54)
        print("   PARTIDA #" + str(partidas))
        print("-" * 54)

        minimo, maximo = obtener_rango()
        print("\n   Rango definido: " + str(minimo) + " a " + str(maximo))
        print("   Piensa bien tu numero y presiona Enter cuando estes listo.")
        input()

        encontrado, intentos = computador_adivina(minimo, maximo)

        mostrar_resultado(encontrado, intentos)

        if not preguntar_repetir():
            break

    print("\n   Jugaste " + str(partidas) + " partida(s) en esta sesion.")
    print("   Gracias por jugar!")


def main():
    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("   Selecciona una opcion: ").strip()

        if opcion == "1":
            ejecutar_juego()

        elif opcion == "2":
            mostrar_instrucciones()

        elif opcion == "3":
            mostrar_algoritmo()

        elif opcion == "4":
            mostrar_creditos()

        elif opcion == "5":
            print("\n" + "=" * 54)
            print("   Gracias por jugar!")
            print("   Espero haberte impresionado. Hasta la proxima!")
            print("=" * 54 + "\n")
            break

        else:
            print("   Opcion no valida. Elige entre 1 y 5.")
            continue

main()
