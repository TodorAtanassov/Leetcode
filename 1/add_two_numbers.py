l1, l2 = [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]

n1 = ''.join([str(i) for i in l1[::-1]])
n2 = ''.join([str(j) for j in l2[::-1]])

res = int(n1) + int(n2)
res = str(res)

out = [int(k) for k in res[::-1]]
print(out)
