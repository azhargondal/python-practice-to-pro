# Problem: Given a string, return it reversed.
# Input: "hello"
# Output: "olleh"

def rverse_string1(s):
    reversed_s = ""
    # range(start, stop, step) generates
    for i in range(len(s) - 1, -1, -1):
        #  print(i, s[i])
        reversed_s += s[i]
    print(reversed_s)


def reverse_string_two_pointers(s):
    charlist = list(s)
    left = 0 
    right = len(s)-1

    while left < right:
        charlist[left], charlist[right] = charlist[right], charlist[left]
        left += 1
        right -= 1

    reverse = "".join(charlist)
    print(reverse)


def reverse_string_slicing(s):
    return s[::-1]


def reverse_string_recursive(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1])
    
# reverse_string_slicing("AzharMehmood")

print(reverse_string_recursive("AzharMehmood"))
