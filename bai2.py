import numpy as np
m=int(input())   
n=int(input())
a = [[int(input()) for i in range(n)] for j in range(m)]
arr=np.array(a)
print("gia tri nho nhat cua cot:", arr.min(0))
print("gia tri lon nhat cua hang: ", arr.max(1))
print("tong so tren duong cheo chinh:", arr.trace())