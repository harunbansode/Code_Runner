from typing import List
# def convertTemperature(celsius: float) -> List[float]:
#     Kelvin = celsius + 273.15
#     Fahrenheit = celsius * 1.80 + 32.00
#     ans = [Kelvin, Fahrenheit]
#     return ans


# print(convertTemperature(36.50))


# def sum(num1: int, num2: int) -> int:
#     ans = num1 + num2
#     return ans

# num1 = -10
# num2 = 4
# print(sum(num1, num2))


def numIdenticalPairs(nums: List[int]) -> int:
    new_num = []
    for i in range(0, len(nums)):
        print(nums[i])



nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))