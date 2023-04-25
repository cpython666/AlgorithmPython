# https://leetcode.cn/problems/spiral-matrix-ii/

# 给你一个正整数n ，生成一个包含1到n2所有元素，且元素按顺时针顺序螺旋排列的nxn正方形矩阵matrix 。
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0]*n for i in range(n)]
        x,y=0,0
        cur=1
        dx,dy,dir=[0,1,0,-1],[1,0,-1,0],0
        while cur<=n**2:
            ans[x][y]=cur
            a,b=x+dx[dir],y+dy[dir]
            if a<0 or a>=n or b<0 or b>=n or ans[a][b]!=0:
                dir=(dir+1)%4
                a,b=x+dx[dir],y+dy[dir]
            x,y=a,b
            cur+=1
        return ans

solution=Solution()
ans=solution.generateMatrix(8)
for i in ans:
    print(i)