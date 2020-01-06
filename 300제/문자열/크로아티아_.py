cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
t = input()

for key in cro:
    t = t.replace(key, '_')
print(len(t))
