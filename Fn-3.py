'''Fn-3 Unicos'''

def removerTodosRepetidos(arr):
    #arr=[9,3,1,3,2,9,]
    arrN=[]

    for j in range (len(arr)):
        contador=0
        for i in range (0,len(arr)):
            if arr[j]==arr[i]:
                contador+=1 
        if contador==1:   
            arrN.append(arr[j])
    return arrN

def main():
    arr=[9, 3 ,1, 3, 9, 2, 3, 9]
    print("El arreglo original es: ", arr)
    print("Eliminando solamente repetidos: ", removerTodosRepetidos(arr))


if __name__ == '__main__':
    main()