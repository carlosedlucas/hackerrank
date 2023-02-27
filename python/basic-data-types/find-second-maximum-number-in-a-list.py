if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr_sorted = sorted(arr)
maximo = max(arr_sorted)

for i in range(0, len(arr_sorted)):
    if maximo in arr_sorted:
        arr_sorted.remove(maximo)

print(arr_sorted[-1])
