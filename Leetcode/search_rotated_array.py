# def search(nums, target):
#     found = -1
#
#     if len(nums) < 4:
#         if target in nums:
#             found = nums.index(target)
#             return found
#         else:
#             return -1
#     m = 0
#     for i in range(len(nums)):
#         if nums[m] <= nums[i]:
#             m = i
#         else:
#             m = i-1
#             break
#     left = 0
#     right = len(nums) - 1
#     # a = nums[m]
#     if nums[m+1] > target >= nums[0]:
#         right = m
#     if nums[m] <= target < nums[0]:
#         left = m
#     if nums[m] == nums[-1]:
#         left = 0
#         right = len(nums) - 1
#     mid = 0
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] > target:
#             right = mid - 1
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             found = mid
#             break
#     # print(found)
#     return found
#
#
# print(search([4, 5, 6, 7, 8, 1, 2, 3], 8))
#
#
#
#
def search(arr, l, h, key):
    if l > h:
        return -1

    mid = (l + h) // 2
    if arr[mid] == key:
        return mid  
    if arr[l] <= arr[mid]:

        if arr[l] <= key <= arr[mid]:
            return search(arr, l, mid - 1, key)
        return search(arr, mid + 1, h, key)

    if arr[mid] <= key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid - 1, key)


arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
i = search(arr, 0, len(arr) - 1, key)

