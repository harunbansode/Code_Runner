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

s = (input())
print(romanToInt(s))

# def romanToInt(s1: str) -> int:
#     translation = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000,
#     }

#     s1 = s1.replace("IV", "IIII").replace("IX", "VIIII")
#     s1 = s1.replace("XL", "XXXX").replace("XC", "LXXXX")
#     s1 = s1.replace("CD", "CCCC").replace("CM", "DCCCC")

#     sum = 0
#     for i in s1:
#         sum += int(translation[i])
#     return sum

# s1 = list(input())
# romanToInt(s1)


# translation = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000,
# }


# def romanToInt(s: str) -> int:
#     x = list(input())
#     # print(x)
#     # roman_list = []
#     sum = 0
#     for i in x:
#         # print((s[i]))
#         # roman_list.append(s[i])
#         # print(sum)
#         sum += s[i]
#     print(sum)


    # print(sum(roman_list))
    # roman_list = []
    # for i in x:
    #     print(s[i])
    #     # print(i)
    #     # roman_list = s[i] + roman_list
    #     # roman_list.append(s[i]+ roman_list)
    # print(roman_list)


    #     l = ''
    #     l =+ s[i]
    #     roman_list.append(l)
    # print(roman_list)



# s = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000,
# }

# romanToInt(s)


# # # x = list(input())
# #     # print(x)

# #     for keys, value in s.items():
# #         # print(keys, value)
# #         x = input()
# #         y = input()
# #         z = s[x] + s[y]
# #         print(z)

# def romanToInt(s: str) -> int:

#     translations = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000,
# }

# s = s.replace("IV", "IIII").replace("IX", "VIIII")
# s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
# s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

# sum = 0
# for i in s:
#     sum += translations[i]
#     print(sum)



# # print((s[i]))
#         # roman_list.append(s[i])
#         print(sum)