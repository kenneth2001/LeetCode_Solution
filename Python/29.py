class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = -1 if (dividend < 0) ^ (divisor < 0) else 1
        counter = 0

        dividend = abs(dividend)
        divisor = abs(divisor)
        

        while dividend >= divisor:
            k = 1
            while k * 2 * divisor <= dividend:
                k *= 2
            dividend -= divisor * k
            counter += k
        
        counter = counter * flag

        if counter >= 2147483647:
            return 2147483647
        elif counter <= -2147483648:
            return -2147483648
        
        return counter
