# 基础算法中的典型案列

# 1 汉诺塔问题
def hannota(n):
    if n == 1:
        return 1
    return 2 * hannota(n - 1) + 1


# 2 二分查找[前提是所查找的列表必须为有序列表]
def binary_search(dataset, value):
    left = 0
    right = len(dataset)
    while left <= right:
        mid = (left + right) // 2
        if dataset[mid] == value:
            return mid
        elif dataset[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return None


#3 冒泡排序
def maopao(dataset):
    temp_dataset = dataset.copy()
    while len(temp_dataset) > 1:
        n = 0
        while n < len(temp_dataset) - 1:
            if temp_dataset:
                pass


if __name__ == "__main__":
    res = hannota(6)
    print(res)