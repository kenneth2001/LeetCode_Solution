class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(base, power):
            if base == 0:
                return 0
            if power == 0:
                return 1
            if power == 1:
                return base
               
            tmp = calculate(base, power // 2)
            if power % 2 == 0:
                return tmp * tmp
            else:
                return tmp * tmp * base
            
        if n < 0:
            ans = calculate(x, -n)
            return 1 / ans
        else:
            return calculate(x, n)
            