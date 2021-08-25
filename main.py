from multiprocessing import Process,cpu_count
import time
import random

def llenarArray():
    lista = []
    cont = 0
    while cont < 1000000:
        lista.append(random.randint(1,1000000))
        cont += 1
    return lista

def intercambio(lista):
    for i in range(0, len(lista)):
        for j in range(i, len(lista)):
            if lista[i] > lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp

def quicksort(lista,inicio,fin):
    if fin <= inicio:
        return
    pivot = lista[fin]
    i = inicio - 1
    for j in range(inicio,fin):
        if lista[j] < pivot:
            i += 1
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
    i += 1
    temp = lista[i]
    lista[i] = lista[fin]
    lista[fin] = temp

    quicksort(lista, inicio, i - 1)
    quicksort(lista, i + 1, fin)



def main():
    lista = llenarArray()
    #intercambio(lista)
    lista.sort()
    #quicksort(lista,0,len(lista)-1)

    # for i in lista:
    #     print(i)
    print("La aplicación se ejecuto en:",time.perf_counter())

#Conclusión: Esta muy bueno el TimSort que usa python

if __name__ == '__main__':
    main()