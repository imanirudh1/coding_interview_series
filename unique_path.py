def unique_path(m, n):
    N = m + n - 2
    r = m - 1
    res=1
    for i in range(1, r + 1):
        res = res * (N - r + i) / i
    return int(res)
    
print(unique_path(3, 7))

#  def uniquePaths(self, m, n):
#         aux = [[1 for x in range(n)] for x in range(m)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 aux[i][j] = aux[i][j-1]+aux[i-1][j]
#         return aux[-1][-1]

# A 2D aux array is redundant. 1D is enough.

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [1] * n
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[j] = dp[j - 1] + dp[j]
#         return dp[-1] if m and n else 0