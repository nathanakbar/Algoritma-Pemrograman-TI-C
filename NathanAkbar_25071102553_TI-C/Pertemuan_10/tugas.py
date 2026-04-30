
data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505,
        123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234,
        42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76,
        166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]


# RADIX SORT

def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr


# MERGE SORT

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# LINEAR SEARCH

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i, arr[i]
    return -1, None


# BINARY SEARCH

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, None


# MAIN PROGRAM

print("Data sebelum sorting:")
print(data)

# Radix Sort
radix_sorted = radix_sort(data.copy())

print("\nHasil Radix Sort:")
print(radix_sorted)

# Merge Sort
merge_sorted = merge_sort(data.copy())

print("\nHasil Merge Sort:")
print(merge_sorted)


# INPUT USER

target = int(input("\nMasukkan angka yang ingin dicari: "))

# Linear Search
idx_lin, val_lin = linear_search(data, target)
if idx_lin != -1:
    print(f"\n[Linear Search] Data ditemukan di index {idx_lin} dengan nilai {val_lin}")
else:
    print("\n[Linear Search] Data tidak ada")

# Binary Search (pakai data yang sudah di-sort)
idx_bin, val_bin = binary_search(merge_sorted, target)
if idx_bin != -1:
    print(f"[Binary Search] Data ditemukan di index {idx_bin} dengan nilai {val_bin}")
else:
    print("[Binary Search] Data tidak ada")
