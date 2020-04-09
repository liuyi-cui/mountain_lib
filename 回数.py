def is_palindrome(n):

    m=str(n)
    while True:
        if len(m) <= 1:
            return True
        else:
            if m[0] == m[-1]:
                m = m[1:-1]
            else:
                return False

# 测试:

output = filter(is_palindrome, range(1, 1000))

print('1~1000:', list(output))

if list(filter(is_palindrome, range(1, 200)))==[1, 2, 3, 4, 5, 6, 7, 8, 9,11, 22, 33, 44, 55, 66, 77, 88, 99,101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:

    print('测试成功!')

else:

    print('测试失败!')