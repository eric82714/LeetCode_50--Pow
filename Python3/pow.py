class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1: return 1
        if x == 0: return 0
        
        if n < 0:
            x = 1 / x
            n = abs(n) 
        
        half = self.myPow(x, int(n/2))
        
        if n % 2 == 1: return half * half * x
            
        return half * half
