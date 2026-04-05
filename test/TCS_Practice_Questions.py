
''' sum DIGITS in a string '''

def sumDigits(s: str):
    
    ans = 0
    for ch in s:
        if ch.isdigit():
            ans += int(ch) # [ ans += s.charAt(i)-'0' ]

    print(ans) # 10

# sumDigits(input())

########################################

''' sum NUMBERS in a string '''

def sumNumbers(s: str):

    ans = 0
    i = 0

    while i<len(s):
        if s[i].isdigit():
            num = 0

            while i<len(s) and s[i].isdigit():
                num = num*10 + int(s[i]) # [ num = num*10 + (s.charAt(i)-'0'); ]
                i += 1

            ans += num
        else:
            i += 1

    print(ans)

# sumNumbers(input())

########################################

''' Reverse WORDS in a string '''

def reverseWords(s: str):

    ans = ""
    words = s.split() # [ String[] words = s.split() or s.split("\\s+") ]

    i=0; j=len(words)-1
    while i<j:
        temp = words[i]
        words[i] = words[j]
        words[j] = temp
        i+=1
        j-=1

    s = " ".join(words) # [ String.join(" ", words); ]
    print(s)

# reverseWords(input())

########################################

''' Find 1st non repeating character '''

def firstNonRepeatingChar(s: str):
    st = set()
    ans = ""
    for c in s:
        if c not in st:
            st.add(c)
        else:
            ans = c
            break

    print(ans)

# firstNonRepeatingChar(input())

########################################

''' fibonacci number - without recursion'''

def fibonacci(n: int):
    if n<=0:
        print("")
        return
    
    if n==1:
        print(0)
        return
    
    a = 0; b = 1
    ans = []

    for _ in range(n):
        ans.append(a)
        a, b = b, a+b

    print(" ".join(map(str, ans))) # convert to string before joining

# fibonacci(int(input()))


#! fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        set = {0:0, 1:1}
        def f(x):
            if x in set:
                return set[x]
            else:
                set[x]=f(x-1)+f(x-2)
                return set[x]

        return f(n)
    
#! Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        set = {0:0, 1:1, 2:1}
        def f(x):
            if x in set:
                return set[x]
            else:
                set[x] = f(x-1) + f(x-2) + f(x-3)
                return set[x]
        return f(n)

########################################

''' Factorial - without recursion '''

def factorial(n: int):

    ans = 1

    while(n>1):
        ans = ans*n
        n -= 1

    print(ans)

# factorial(int(input()))

########################################

''' Longest word in a sentence '''

def longestWord(s: str):

    words = s.split()
    n = len(words)

    maxWord = ""
    for i in range(n):
        if len(words[i]) > len(maxWord):
            maxWord = words[i]
    
    print(maxWord)

# longestWord(input())

########################################

''' Toggle case of characters '''

def toggleCase_method1(s: str):
    return s.swapcase()


def toggleCase_method2(s: str):
    res = []

    for ch in s:
        if ch.islower():  # java: isLowerCase()
            res.append(ch.upper()) # java: toUpperCase()
        elif ch.isupper():
            res.append(ch.lower())
        else:
            res.append(ch) # keep digits / symbols unchanged
    
    return "".join(res)


# public static toggleCase_method3(String s){
#     StringBuilder res = new StringBuilder();
#     for(char ch: s.toCharArray()){
        
#         if(ch >= 'a' && ch <= 'z'){
#             res.append((char)(ch - 32)); // to uppercase
#         }else if(ch >= 'A' && ch <= 'Z'){
#             res.append((char)(ch + 32)); // to lowercase
#         }else{
#             res.append(ch);
#         }
#     }
#     return res.toString();
# }

# print(toggleCase_method1(input()))
print(toggleCase_method2(input()))

#####################################################

''' GCD / HCF of two numbers '''

def gcd(a: int, b: int) -> int: # Euclidean Algorithm
    if(b == 0):
        return a
    return gcd(b, a%b)

#####################################################

''' LCM of two numbers '''

def lcm(a: int, b: int) -> int:
    return int(a*b/gcd(a,b))

print(gcd(20,4))
print(lcm(20,4))

