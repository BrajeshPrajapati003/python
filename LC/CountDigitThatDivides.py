# 2520 -> Count the Digits That Divide a Number

def countDigits(self, num: int) -> int:
        if num == 0: return num
        digitCount = 0
        temp = num
        while(num > 0):
            digit = num % 10
            if temp%digit == 0:
                digitCount += 1
            num //= 10 # num /= 10 -> float division can give (not int) wrong answer
        return digitCount

