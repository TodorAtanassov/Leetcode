num = 'MCMXCIV'
num = num.replace('IV', 'F'), num.replace('IX', "N"), \
      num.replace('XL', 'T'), num.replace('XC', 'Y'), num.replace('CD', 'H'), num.replace('CM', 'O')
s = num[len(num)-3]
rom = {'I': 1,
       'V': 5,
       'X': 10,
       'L': 50,
       'C': 100,
       'D': 500,
       'M': 1000,
       'F': 4,
       "N": 9,
       'T': 40,
       'Y': 90,
       'H': 400,
       'O': 900,
       }
print(s)
# output = 0
# for i in s:
#     output += rom.get(i, i)
#
# print(output)
