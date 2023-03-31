from typing import List

def search(nums: List[int], target: int) -> int:
    for i in range(0, len(nums)):
        # print(f'{nums[i]} is index of {i}')
        if nums[i] == target:
            return i
    return -1

nums= [-1,0,3,5,9,12]
target = 2
print(search(nums, target))













# def search(nums, target):
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# print(search([-1,0,3,5,9,12], 9)) # Output: 4
# print(search([-1,0,3,5,9,12], 2)) # Output: -1
