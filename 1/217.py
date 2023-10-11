# nums = [1, 2, 3, 1]
# nums1 = [1, 2, 3, 4]
# nums2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
#
#
# def dupl(lst):
#     return len(set(lst)) != len(lst)
#
#
# print(dupl(nums))
# print(dupl(nums1))
# print(dupl(nums2))

prices = [3, 8, 1, 4, 7, 5]

for i in prices:
    for j in prices[prices.index(i)+1:]:
        print(j - i, end=' ')
    print()

# def get_price(sortd):
#     sortd[1]
