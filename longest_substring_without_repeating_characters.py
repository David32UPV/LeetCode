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

        elemento_repetido = False
        indice_elemento_repetido = 0
        longitud_sliced_window = []

        # Al final me tengo que guardar el maximo de 2 subarrays
        for i in range(indice_elemento_repetido, len(array_char)):
            if array_char[i] not in sliced_window:
                sliced_window.append(array_char[i])
                elemento_repetido = False
            else:   
                elemento_repetido = True
                sliced_window.append(array_char[i])
                indice_elemento_repetido = len(sliced_window) -1 - sliced_window[::-1].index(array_char[i])
                longitud_sliced_window.append(len(sliced_window))
                del sliced_window[:indice_elemento_repetido-1]

        if elemento_repetido == True:
            return max(longitud_sliced_window)
        else:
            return len(sliced_window)
        
# Solo se ejecuta lo que hay debajo de este if en este programa y NO en otro programa que importe este programa
if __name__ == "__main__":
    solucion = Solution()
    input_string = "bbbbb"
    string_resultado = solucion.lengthOfLongestSubstring(input_string)

    print(string_resultado)
