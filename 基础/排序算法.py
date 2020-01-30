#分别用选择排序法，冒泡排序法和插入排序法将列表[1, 3, 1, 4, 5, 2, 0]中的数从小到大排序

#选择排序法
def selectionSort(arr):
    # 求出arr的长度
    n = len(arr)
    # 外层循环确定比较的轮数，x是下标，arr[x]在外层循环中代表arr中所有元素
    for x in range(n - 1):
        # 内层循环开始比较
        for y in range(x + 1, n):
            # arr[x]在for y 循环中是代表特定的元素，arr[y]代表任意一个arr任意一个元素。
            if arr[x] > arr[y]:
                # 让arr[x]和arr列表中每一个元素比较，找出小的
                arr[x], arr[y] = arr[y], arr[x]
    return arr
print(selectionSort([1, 3, 1, 4, 5, 2, 0]))

#冒泡排序法
def bubbleSort(arr):
    n = len(arr)
    for x in range(n - 1):
        for y in range(n - 1 - x):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
    return arr
print(bubbleSort([1, 3, 1, 4, 5, 2, 0]))

#插入排序法
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print(insertionSort([1, 3, 1, 4, 5, 2, 0]))
