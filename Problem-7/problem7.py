class Solution:
    def reverse(self, x: int) -> int:
        pass
    
    
# Method 1
def reverseInteger(x):
    result = 0
    if x > 0:
        sign = 1
    else:
        sign = -1 
    x = x * sign   
    while x > 0:
        result = result * 10 + x % 10
        x //= 10
    result = result * sign
    return result if result >= -(2**31) and result <= (2**31 - 1) else 0


# print(reverseInteger(1234))
# print(reverseInteger(-123))


def reverseDigits(x):
    result = 0
    if x > 0:
       sign = 1
    else:
       sign = -1
    x = abs(x)
    while x > 0:
        result = result * 10 + x % 10
        x = x // 10
    result = result * sign
    return result if result >= -(2**31) and result <= (2**31 - 1) else 0

print(reverseDigits(1234))
print(reverseDigits(-123))

# Method 2
def reverse(x) -> int:
    y = str(abs(x))
    res = y[::-1]
    if x > 0:
        sign = 1
    else:
        sign = -1
    ans = int(res) * sign
    return ans 

# print(reverse(1234))
# print(reverse(-123))