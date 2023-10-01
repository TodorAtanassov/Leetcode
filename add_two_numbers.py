l1, l2 = [2, 4, 3], [5, 6, 4]

n1 = ''.join([str(i) for i in l1[::-1]])
n2 = ''.join([str(j) for j in l2[::-1]])

res = int(n1) + int(n2)
res = str(res)

out = [int(k) for k in res[::-1]]
print(out)