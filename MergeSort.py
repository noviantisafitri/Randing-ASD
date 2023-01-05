import os
os.system('cls')


def mergesort(list):
    list_length = len(list)
    if list_length <= 1:
        return list

    mid = list_length // 2
    left = mergesort(list[:mid])
    right = mergesort(list[mid:])
    return merge(left, right)

def merge(l, r):
    output = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            output.append(l[i])
            i += 1
        else:
            output.append(r[j])
            j += 1
    output.extend(l[i:])
    output.extend(r[j:])

    return output

def pisah(listku): 
    pisahkan = [] 
    for i in listku: 
        if isinstance(i, list):
            pisahkan.extend(pisah(i))
        else: 
            pisahkan.append(int(i)) 
    return pisahkan

variable = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]

print("Merge Sort")
print("Sebelum = ",variable) 
hasil = pisah(variable) 
print("Setelah dipisah = ",hasil) 
sort = mergesort(hasil)
print("Setelah disorting =", sort)
