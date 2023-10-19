#Metodo de Ordenamiento de Burbuja (Bubble Sort)

def bubbleSort (nums):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range (len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1], nums[i+1], nums[i]
                intercambio = True

listaNumerica = [5, 2, 1, 8, 4]
print("Lista original: " + str(listaNumerica))
bubbleSort(listaNumerica)
print("Lista ordenada: " + str(listaNumerica))