from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
        check_list = str(strs[0][:2])
        for i in range(1, len(strs)):
            if strs[i] >= 1:
                 if strs[i][:2] == check_list:
                  return check_list
        return ''

#strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))




# check_list = str(strs[0][:2])
#         # print(check_list)
#         for i in range(1, len(strs)):
#             if strs[i][:2] == check_list:
#                 return check_list
#         return ''