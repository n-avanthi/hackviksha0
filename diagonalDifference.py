def diagonalDifference(arr):
    prim = 0
    sec = 0
    length = len(arr[0])
    for count in range(length):
        prim += arr[count][count]
        sec += arr[count][(length-count-1)]
    print(abs(prim-sec))
#main
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
result = diagonalDifference(arr)