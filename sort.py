
def bubbleSort(data):

    n = len(data)
    for i in range(n):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def selectionSort(data):

    n = len(data)
    for i in range(n):
        for j in range(i+1, n):
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]
    return data

def merge(leftData, rightData):

    mergedData = []

    n1 = len(leftData)
    n2 = len(rightData)

    index1 = index2 = 0

    while index1 < n1 and index2 < n2:
        if leftData[index1] < rightData[index2]:
            mergedData.append(leftData[index1])
            index1 += 1
        else:
            mergedData.append(rightData[index2])
            index2 += 1

    mergedData += leftData[index1:]
    mergedData += rightData[index2:]

    return mergedData

def mergeSort(data):

    if len(data) < 2:
        return data

    mid = len(data)//2

    leftData = mergeSort(data[:mid])
    rightData = mergeSort(data[mid:])
    mergedData = merge(leftData, rightData)

    return mergedData


def quickSort(data, start, end):

    if start >= end:
        return data

    key = start
    index1 = start
    index2 = end

    while index1 < index2:
        while index1 < index2 and data[index2] >= data[key]:
            index2 -= 1

        while index1 < index2 and data[index1] <= data[key]:
            index1 += 1

        data[index1], data[index2] = data[index2], data[index1]
    print(index1, index2)
    data[key], data[index2] = data[index2], data[key]

    quickSort(data, start, index1-1)
    quickSort(data, index1+1, end)

    return data

def QuickSort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key =left
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= lists[key]:#如果右边比基准小，停下
            right -= 1
        while left < right and lists[left] <= lists[key]:#如果左边比基准大，停下
            left += 1
        lists[right],lists[left]=lists[left],lists[right]#交换现在的左右值
    print(left, right)
    lists[right] ,lists[key]=lists[key],lists[right] #left和right汇合后和基准交换

    QuickSort(lists, low, left - 1)
    QuickSort(lists, left + 1, high)
    return lists




if __name__ == '__main__':

    data = [2,4,1,10,8,18]
    #data = bubbleSort(data)
    #data = selectionSort(data)
    #data = mergeSort(data)
    data = quickSort(data,0, len(data)-1)
    #data = QuickSort(data, 0, len(data)-1)
    print(data)