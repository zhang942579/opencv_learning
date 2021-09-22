import numpy as np

n = int(input('输入：'))


arr = np.random.randint(0, 10, [n, n])
print(arr)
lis = np.split(arr, n, axis=0)
for item in lis:
    item.sort(axis=1)
arr = np.vstack(lis)
for item in lis:
    item.sort(axis=0)

arr = np.hstack(lis)
print(arr)



