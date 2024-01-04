def suma_dos_numeros(num1, num2):
    """
    Recibe dos números y devuelve su suma.
    """
    suma = num1 + num2
    return suma

def doblar_valores_en_sitio(lista):
    """
    Recibe una lista y modifica esa misma lista (referencia) doblando los valores de todos los elementos.
    No devuelve nada.
    """
    for i in range(len(lista)):
        lista[i] *= 2

def doblar_valores_copia(lista):
    """
    Recibe una lista y devuelve una copia de la lista (referencia) doblando los valores de todos los elementos.
    La lista original no debe modificarse.
    """
    # Realizar una copia profunda de la lista utilizando el módulo copy
    lista_copia = lista.copy()

    # Doblar los valores en la copia
    for i in range(len(lista_copia)):
        lista_copia[i] *= 2

    return lista_copia

# Ejemplo de uso
num1 = 5
num2 = 7
resultado_suma = suma_dos_numeros(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado_suma}")

lista_original = [1, 2, 3, 4]
print(f"Lista original antes de doblar en sitio: {lista_original}")
doblar_valores_en_sitio(lista_original)
print(f"Lista original después de doblar en sitio: {lista_original}")

lista_copia = [1, 2, 3, 4]
lista_copia_doblada = doblar_valores_copia(lista_copia)
print(f"Lista original: {lista_copia}")
print(f"Copia de la lista con valores doblados: {lista_copia_doblada}")
