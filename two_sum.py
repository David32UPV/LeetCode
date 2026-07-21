from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Tengo que sacar los indices de 2 numeros de nums tal que
        # la suma de esos 2 numeros de target

        """----- SOLUCION FUERZA BRUTA -------
        # for (int i = 0; i < nums.length(); i++) 
        for i in range(len(nums)):
            # for (int j = i; j < nums.length(); j++)
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target) and (i is not j):
                    # i++ va antes que j++ por lo que al final del bucle j se imprime antes
                    vector_solucion: List[int] = [j, i]

       return vector_solucion
        """

        #--- SOLUCION OPTIMIZADA -----
        "enumerate() recorre una coleccion y obtiene el indice y el valor de cada elemento al mismo tiempo"
        diccionario_busqueda = {}
        for indice, valor in enumerate(nums):
            clave = valor
            # Tengo que encontrar un numero b tal que nums[i] + b = target
            b = target - clave
            
            # Hay que convertir el array original en una tabla hash o diccionario para que la busqueda sea mas rapida (O(n))
            # Las claves son los indices del array
            if b in diccionario_busqueda:       # O(1)
                vector_solucion = [diccionario_busqueda[b], indice]
            else:
                # Guardo el elemento actual si no he encontrado b en el diccionario, lo cual siempre se ejecuta en la 1ª iteracion 
                diccionario_busqueda[clave] = indice
        return vector_solucion
    
if __name__ == "__main__":
    solucion = Solution()

    lista_nums = [3, 3]
    objetivo = 6

    resultado = solucion.twoSum(lista_nums, objetivo)

    print(resultado)

        