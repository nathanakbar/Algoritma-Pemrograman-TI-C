while True:
    jumlah_elemen = int(input(f"Masukkan jumlah elemen: "))

    if jumlah_elemen <= 0:
        print("Jumlah elemen tidak boleh nol atau kecil dari nol\n")
    else:
        break

array = []

i = 0
while True:
    temp = int(input(f"Masukkan elemen ke {i+1}: "))

    if temp >= 0:
        array.append(temp)
        i+=1
        if len(array) == jumlah_elemen:
            break
    else:
        print("Tidak boleh negatif\n")


def insertion_sort(data):
    data = data.copy()
    for i in range(1, len(data)):
        current_value = data.pop(i)
        insert_index = i

        for j in range(i-1, -1, -1):
            if data[j] > current_value:
                insert_index = j

        data.insert(insert_index, current_value)

    return data

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i + 1


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

    return array



def countingSort(arr):
    arr = arr.copy()
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr



print("Insertion Sort:", insertion_sort(array))
print("Quick Sort:", quicksort(array.copy()))
print("Counting Sort:", countingSort(array))