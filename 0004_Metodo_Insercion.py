#Metodo de Orden Insercion (Insert Sort)

def insertionSort(nums):
    
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i-1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = item_to_insert

listaNumeros = [5, 2, 1, 8, 4]
print("Lista sin orden: " + str(listaNumeros))
insertionSort(listaNumeros)
print("Lista ordenada: " + str(listaNumeros))