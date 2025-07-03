# Problem: Count the number of vowels in a string.
# Input: "banana"
# Output: 3


# Problem2: Replace all vowels in the string with *.
# Input: "openAI"
# Output: "*p*n**"

def countvowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    for i in s.lower():
        if i in vowels:
            counter +=1 

    return counter


def count_vowels_recursive(s):
    vowels = "aeiouAEIOU" 
    if s == "": 
        return 0
    if s[0] in vowels:
        return 1 + count_vowels_recursive(s[1:])
    else:
        return count_vowels_recursive(s[1:])
    

def replacevowels(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] 
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i] = "*"

    rv = "".join(s_list)
    return rv

print(replacevowels("bAnana"))