def partition(arr, size, pivot):
    less = []
    equal = []
    greater = []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    result = less + equal + greater
    return result

#main
size = int(input())
if size == 0:
    print("-1")
else:
    arr = list(map(int, input().split()))
    pivot = arr[0]  # The pivot element is the first element of the array
    result = partition(arr, size, pivot)
    print(' '.join(map(str, result)))