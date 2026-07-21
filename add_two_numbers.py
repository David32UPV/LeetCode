from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        aux_1 = l1
        aux_2 = l2

        l3 = ListNode()
        aux_3 = l3
        acarreo = 0

        while (aux_1 is not None or aux_2 is not None):
            # El valor de los nodos va de 0 a 9

            valor_nodo_1 = 0 if aux_1 is None else aux_1.val 
            valor_nodo_2 = 0 if aux_2 is None else aux_2.val

            suma_nodos = (valor_nodo_1 + valor_nodo_2) % 10
            acarreo_siguiente = (valor_nodo_1 + valor_nodo_2 + acarreo) // 10

            valor_nodo_lista_3 = 0 if suma_nodos + acarreo > 9 else suma_nodos + acarreo
    
            aux_3.next = ListNode(valor_nodo_lista_3)

            if aux_1 is not None:
                aux_1 = aux_1.next

            if aux_2 is not None:    
                aux_2 = aux_2.next                

            aux_3 = aux_3.next

            acarreo = acarreo_siguiente

        # Si llega un punto en que las 2 listas son nulas, l3 tendra un nuevo nodo si arrastra un acarreo
        # aux_3 es el nodo actual y l3 es el nodo que apunta a la cabeza de la lista
        if acarreo > 0:
            aux_3.next = ListNode(acarreo)
        
        # Devolvemos los nodos que hay después del primero que nos creamos antes del while que se inicializa con val = 0
        return l3.next
    
def crear_lista_enlazada(valores: List[int]) -> ListNode:
    le = ListNode(valores[0], None)
    aux = le # aux empieza apuntando a la cabeza de la lista

    for valor in valores[1:]:
        aux.next = ListNode(valor)
        aux = aux.next

    return le

if __name__ == "__main__":
    solucion = Solution()

    lista_1 = [9,9,9,9,9,9,9]
    lista_2 = [9,9,9,9]

    l1 = crear_lista_enlazada(lista_1)
    l2 = crear_lista_enlazada(lista_2)

    resultado = solucion.addTwoNumbers(l1, l2)

    nodo_cabeza = resultado
    while nodo_cabeza is not None:
        print(f"Nodo actual -> ", nodo_cabeza.val)
        nodo_cabeza = nodo_cabeza.next