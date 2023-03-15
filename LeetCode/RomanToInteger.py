def romanToInt(s: str) -> int:
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    s1 = list(s)
    translation = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    }
    sum = 0
    for i in s1:
        sum += int(translation[i])
    return sum

s = input()
print(romanToInt(s))