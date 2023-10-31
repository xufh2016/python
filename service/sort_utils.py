def bubble_sort(arr):
    """
    定义一个冒泡排序
    :param arr: iterable
    :return:  序列
    """
    # if not isinstance(arr, list):
    #     return
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [34, 4, 12, 64, 1, 88, 33, 56]
arr1 = bubble_sort(arr)
print(arr1)
