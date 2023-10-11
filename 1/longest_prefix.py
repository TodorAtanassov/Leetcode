strs = ["flower", "flow", "flight"]


# def longestCommonPrefix(lst):
#     res = ""
#     for a in zip(*strs):
#         if len(set(a)) == 1:
#             res += a[0]
#         else:
#             return res
#     return res


def longestCommonPrefix(lst):
    if len(lst) == 0:
        return ''
    base = lst[0]

