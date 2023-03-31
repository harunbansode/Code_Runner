from typing import List
def restoreString(s: str, indices: List[int]) -> str:

    mod_b=[None]*len(s)
    for i,x in enumerate(indices):
        mod_b[x]=s[i]
    return ("".join(mod_b))

s = "codeleet"
indices =  [4, 5, 6, 7, 0, 2, 1, 3]
print(restoreString(s, indices))
















# shuffle_string = [t[1] for t in sorted(zip(indices,s))]
    # s1 = str(shuffle_string)
    # print(s1)
    # return s1


# shuffle_string = ''
# for i in str(sorted(zip(indices, s))):
#     shuffle_string += i
# return shuffle_string


# shuffle_string = []

#     for i in range(0, len(indices)):
#         shuffle_string.insert(indices[i], s[i])
#         print(shuffle_string)
#     return shuffle_string