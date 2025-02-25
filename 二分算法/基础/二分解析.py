
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left


# 多数字场景
arr = [1,2,4,9,10]
# target>max(arr)
print(binary_search(arr, 2))
# target<min(arr)
print(binary_search(arr, 5))
# 找最左边的3
print(binary_search(arr, 3))
# 找最右边的3