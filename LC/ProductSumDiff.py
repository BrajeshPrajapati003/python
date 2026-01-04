#  1281 -> Subtract the Product and Sum of Digits of an Integer

def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        while(n > 0):
            digit = n%10
            sum += digit
            product *= digit
            n //= 10
        return product - sum

