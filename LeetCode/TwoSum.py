from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    indices = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                indices.append(i)
                indices.append(j)
                return indices

nums = [2, 7, 11 , 15]
target = 17
print(twoSum(nums, target))