# Frecuencias típicas del español (solo mayúsculas)
frecuencias_esp = {
    'A': 11.96, 'B': 0.92, 'C': 2.92, 'D': 6.87, 'E': 16.78, 'F': 0.52, 'G': 0.73, 'H': 0.89,
    'I': 4.15, 'J': 0.3, 'K': 0.0, 'L': 8.37, 'M': 2.12, 'N': 7.01, 'Ñ': 0.29, 'O': 8.69,
    'P': 2.776, 'Q': 1.53, 'R': 4.94, 'S': 7.88, 'T': 3.31, 'U': 4.8, 'V': 0.39, 'W': 0.0,
    'X': 0.06, 'Y': 1.54, 'Z': 0.15
}
frecuencias_esp = sorted(frecuencias_esp.items(), key=lambda x: x[1], reverse=True)

# Función principal
def main():
    mensaje = input("Introduce el mensaje cifrado: ")  # Aceptamos mensaje tal cual (con minúsculas y mayúsculas)
    mensaje = mensaje.upper()  # Convertimos a mayúsculas

    # Contamos las letras
    contador = {}
    total_letras = 0
    for letra in mensaje:
        if letra.isalpha():
            if letra not in contador:
                contador[letra] = 0
            contador[letra] += 1
            total_letras += 1

    print(len(contador), " hizki desberdin aurkitu dira.")

    # Calculamos la frecuencia de las letras
    frecuencias = {letra: (cuenta / total_letras) * 100 for letra, cuenta in contador.items()}
    frecuencias = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    # Crear el mapeo de sustitución inicial
    mapeo_sustitucion = {}
    for (letra_mensaje, _), (letra_esp, _) in zip(frecuencias, frecuencias_esp):
        mapeo_sustitucion[letra_mensaje] = letra_esp
    print(mapeo_sustitucion)

    # Función para aplicar sustituciones
    def aplicar_sustituciones(mensaje, sustituciones):
        mensaje_descifrado = []
        for letra in mensaje:
            if letra.isalpha():
                mensaje_descifrado.append(sustituciones.get(letra, letra))
            else:
                mensaje_descifrado.append(letra)
        return "".join(mensaje_descifrado)

    # Aplicar sustituciones iniciales
    mensaje_descifrado = aplicar_sustituciones(mensaje, mapeo_sustitucion)
    print("Mensaje descifrado inicial:", mensaje_descifrado)

    # Interacción con el usuario para realizar sustituciones
    while True:
        print("\nMensaje actual:", mensaje_descifrado)
        sustitucion = input("Introduce la sustitución (formato: letra_descifrada letra_nueva) o 'salir' para terminar: ")
        if sustitucion.lower() == 'salir':
            break
        try:
            letra_descifrada, letra_nueva = sustitucion.split()
            if letra_descifrada.isalpha() and letra_nueva.isalpha() and len(letra_descifrada) == 1 and len(letra_nueva) == 1:
                letra_descifrada = letra_descifrada.upper()
                letra_nueva = letra_nueva.upper()
                
                # Encontrar la letra original que se mapea a letra_descifrada
                letra_original = None
                for k, v in mapeo_sustitucion.items():
                    if v == letra_descifrada:
                        letra_original = k
                        break
                
                if letra_original:
                    # Actualizar el mapeo de sustituciones
                    mapeo_sustitucion[letra_original] = letra_nueva
                    # Aplicar todas las sustituciones acumuladas
                    mensaje_descifrado = aplicar_sustituciones(mensaje, mapeo_sustitucion)
                    print(f"Sustitución realizada: {letra_descifrada} -> {letra_nueva}")
                    print(f"Mapeo actual: {mapeo_sustitucion}")
                else:
                    print(f"No se encontró la letra descifrada {letra_descifrada} en el mapeo actual.")
            else:
                print("Formato incorrecto. Asegúrate de introducir dos letras.")
        except ValueError:
            print("Formato incorrecto. Asegúrate de introducir dos letras separadas por un espacio.")

    # Mostrar el mapeo final antes de salir
    print("Mapeo final:", mapeo_sustitucion)
    print("Mensaje descifrado final:", mensaje_descifrado)

# Ejecutar el programa
if __name__ == "__main__":
    main()

"""
Mensaje final: CON DURRUTI MORIA EL DIRIGENTE QUE, A SU MANERA, MEJOR EXPRESABA COMO COMBATIR AL FASCISMO DESDE UN CRITERIO DE INDEPENDENCIA DE CLASE, A DIFERENCIA DEL COLABORACIONISMO FRENTEPOPULISTA DE LA DIRECCION ANARQUISTA. DURRUTI FUE UN FACTOR DE PRIMER ORDEN EN EL PAPEL DE LA CLASE OBRERA EN CATALUNVA EN JULIO DE 1936. PERO DURRUTI, COMO OCURRE CON LAS PERSONALIDADES EN LA HISTORIA, NO CAVO DEL CIELO. PERSONIFICABA LA TRADICION REVOLUCIONARIA DE LA CLASE OBRERA. SU ENORME POPULARIDAD ENTRE LA CLASE TRABAJADORA, REFLEJADA EN EL ENTIERRO MULTITUDINARIO EN BARCELONA EL 22 DE NOVIEMBRE DE 1936, MUESTRA ESA IDENTIFICACION. SU MUERTE FUE SIN DUDA UN GOLPE OBJETIVO AL PROCESO REVOLUCIONARIO EN MARCHA. SIN DURRUTI QUEDO MAS LIBRE EL CAMINO PARA QUE EL ESTALINISMO, CON LA COMPLICIDAD DEL GOBIERNO DEL FRENTE POPULAR V DE LA DIRECCION ANARQUISTA, TERMINARA EN MAVO DE 1937 LA TAREA DE LIQUIDAR LA REVOLUCION, DESMORALIZANDO A LA CLASE OBRERA V FACILITANDO CON ELLO EL POSTERIOR TRIUNFO FRANQUISTA.


Mapeo final: {'X': 'E', 'E': 'A', 'K': 'R', 'I': 'O', 'C': 'I', 'J': 'N', 'T': 'L', 'A': 'D', 'R': 'C', 'Z': 'U', 'H': 'T', 'N': 'S', 'P': 'M', 'D': 'P', 'Q': 'B', 'O': 'F', 'V': 'V', 'S': 'Q', 'G': 'J', 'U': 'G', 'M': 'H', 'F': 'X', 'L': 'Z'}


"""
