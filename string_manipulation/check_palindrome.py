def check_palindrome(s):
    slist = list(s)
    left = 0
    right = len(s)-1

    while left < right:
        slist[left], slist[right] = slist[right], slist[left]
        left += 1
        right -= 1
    reversed = "".join(slist)
    print(reversed)

    if s == reversed:
        return True
    

def isPalindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1 : len(s) - 1])
    
print(isPalindrome("Azhar"))