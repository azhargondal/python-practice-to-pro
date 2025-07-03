# Problem: Remove all spaces from a string.
# Input: "a b c d e"
# Output: "abcde"

def remove_spaces(rv):
   rv = rv.replace(" ", "")
   print(rv)

def remove_spaces1(s):
   r_s_s = ""

   for i in s:
      if i != " ":
        r_s_s += i
   print(r_s_s)  

remove_spaces1("a b c d e")   