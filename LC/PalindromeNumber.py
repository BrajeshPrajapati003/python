# 9 -> Palindrome Number

# def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#              return False
#         temp = x
#         newNum = 0
#         while(x > 0):
#             newNum = newNum*10 + x%10
#             x //= 10
#         return True if temp == newNum else False


def isPalindrome(self, x: int) -> bool:
        new=str(x)
        return True if new == new[::-1] else False

