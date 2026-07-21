from typing import *

class Solution:

    # Intento solucion optimizada (O(n))
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        diccionario_caracteres = {}
        substring_final: str = ""
        for indice, caracter in enumerate(s):
            clave = caracter
            diccionario_caracteres[clave] = indice

            # Encuentro la ultima posicion del caracter en el diccionario
            if caracter in diccionario_caracteres:
                # Tengo que crearme un DS en el que ir guardando cada valor que me encuentro 
                # Tengo que usar 2 punteros (uno left y otro right y que sean como el i, j en un for)
                left = diccionario_caracteres[clave]
                # Si el indice del caracter actual en el diccionario es > que el indice de la primera ocurrencia de dicho caracter en el mismo,
                # significa que se ha repetido 
                if diccionario_caracteres.values(caracter) > left:
                    pass
        

        return len(substring_final)
    """

    # Intento solucion fuerza bruta (O(n²))
    def lengthOfLongestSubstring(self, s: str) -> int:
        array_char = []
        sliced_window = []

        for char in s:
            array_char.append(char)

        elemento_repetido = 0
        longitud_sliced_window = []

        # Al final me tengo que guardar el maximo de 2 subarrays
        for i in range(elemento_repetido, len(array_char)):
            for j in range(i, len(array_char)):
                if array_char[j] is not array_char[i]:
                    sliced_window.append(array_char[j])
                else:
                    elemento_repetido = array_char.index(array_char[j])
                    longitud_sliced_window.append(len(sliced_window))
                    # Tienes que eliminar cuando se repite algun caracter
                    sliced_window.clear()

        return max(longitud_sliced_window)

# Solo se ejecuta lo que hay debajo de este if en este programa y NO en otro programa que importe este programa
if __name__ == "__main__":
    solucion = Solution()
    input_string = "abcabcbb"
    string_resultado = solucion.lengthOfLongestSubstring(input_string)

    print(string_resultado)
