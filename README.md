# El Computador Adivina Tu Número

## Descripción

>Sistema interactivo desarrollado en Python donde el computador adivina el número que el usuario está pensando, utilizando el algoritmo de búsqueda binaria. El usuario define un rango numérico, piensa un número y responde las preguntas del sistema hasta que éste lo adivina.

## Integrantes

| Nombre | Universidad | Carrera |
|---|---|---|
| Ethan Arellano Villacís | UIDE | Ingeniería en Sistemas de la Información |

## Objetivo del sistema

Desarrollar un sistema funcional en Python que aplique el algoritmo de búsqueda binaria para adivinar un número pensado por el usuario, integrando los contenidos de las cuatro unidades de la asignatura Lógica de Programación: análisis de problemas, diseño de algoritmos, estructuras lógicas y organización del código mediante funciones.

## Descripción de funcionalidades

| Funcionalidad | Descripción |
|---|---|
| Menú principal | Navegación entre todas las opciones del sistema |
| Jugar | El computador adivina el número usando búsqueda binaria |
| Instrucciones | Guía paso a paso para el usuario |
| Cómo funciona el algoritmo | Explicación didáctica de la búsqueda binaria |
| Créditos | Información del proyecto y del estudiante |
| Validación de entradas | Control de errores con `try/except` en todos los ingresos |
| Evaluación de desempeño | Calificación del resultado según los intentos utilizados |
| Múltiples partidas | El usuario puede jugar varias rondas en una misma sesión |

## Estructuras utilizadas

- `while` — bucle del menú principal y control de partidas
- `for` — recorridos internos de validación
- `if / elif / else` — evaluación de respuestas y opciones
- `try / except` — manejo de errores de entrada
- `break` — salida controlada del juego
- `continue` — reintento ante respuesta inválida
- Funciones — organización modular de todo el código

## Algoritmo de búsqueda binaria

```
intento = (minimo + maximo) // 2

Si respuesta == "mayor"  →  minimo = intento + 1
Si respuesta == "menor"  →  maximo = intento - 1
Si respuesta == "correcto"  →  fin del juego
```

Con cada intento se elimina la mitad del rango disponible:
- Rango 1–100 → máximo **7 intentos**
- Rango 1–1000 → máximo **10 intentos**

## Fecha

Período académico: 2026
Entrega final: Semana 8  
Materia: Lógica de Programación — UIDE