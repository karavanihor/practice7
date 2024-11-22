def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
arr = []
n = int(input("Введіть довжину масиву: ")) 
for i in range(0, n): 
    element = int(input("arr[" + str(i + 1) + "] = "))   
    arr.append(element)
bubble_sort(arr) 
print(arr)


def selectionSort( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    return itemsList


def insertion_sort(array): 
    length = len(array) 
    for i in range(1, length):
        key = array[i]
        j = i
        while (j - 1 >= 0) and (array[j - 1] > key):
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        array[j] = key

print("Сортування включенням")
arr = []
length = int(input("Введіть довжину масиву: ")) 
for i in range(0, length): 
    element = int(input("arr[" + str(i + 1) + "] = "))   
    arr.append(element)
insertion_sort(arr) 
print("Відсортований масив: ") 
print(arr)