def isPalindrome(x: int) -> bool:
    num = str(x)
    reverse_str = ''
    for i in range(0, len(num)):
        reverse_str = num[i] + reverse_str 
    if reverse_str == num:
        return True
    else:
        return False


x = 121
print(isPalindrome(x))
