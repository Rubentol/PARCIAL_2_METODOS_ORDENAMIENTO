# Metodo de Orden de Seleccion (Selection Sort)

def selectionSort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j

        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

listaNumeros = [5, 2, 1, 8, 4]
print("Lista sin orden: " + str(listaNumeros))
selectionSort(listaNumeros)
print("Lista ordenada: " + str(listaNumeros))