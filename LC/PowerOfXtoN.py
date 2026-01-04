# 50 -> Pow(x, n)

class Solution:
    def findPow(self, x, n):
        if n == 0:
            return 1
        a = self.findPow(x, n//2)
        if n&1 == 0:
            return a*a
        else:
            return a*a*x

    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            return self.findPow(x,n)
        else:
            return 1/self.findPow(x,-n)
        
