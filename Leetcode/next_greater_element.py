# NOT SOLVED


# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#
#     while low <= high:
#         mid = (high + low) // 2
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return mid
#     return -1
#
#
# arr = [2, 3, 4, 10, 40]
# x = 10
# result = binary_search(arr, x)
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")
#
#
#
#


arr1 = [0]
arr2 = []
arr = []
i, j = 0, 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr.append(arr1[i])
        i += 1
    else:
        arr.append(arr2[j])
        j += 1
arr += arr1[i:] + arr2[j:]
