def matrix():
    n = int(input())
    m = int(input())
    arr = [[int(input()) for i in range(m)] for j in range(n)]
    return arr
def result(A,B,row_A,col_A,row_B,col_B):
    if(col_A!=row_B):
        return None
    c = [[0 for i in range(col_B)] for j in range(row_A)]
    for i in range(row_A):
        for j in range(col_B):
            for k in range(col_A):
                c[i][j]+=A[i][k]*B[k][j]
    return c
A = matrix()
B = matrix()
row_A=len(A)
col_A=len(A[0])
row_B=len(B)
col_B=len(B[0])
print(result(A,B,row_A,col_A,row_B,col_B))

