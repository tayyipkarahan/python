"""
Given a non-empty string and an int n, return a new string where the character at index n has been removed. 
The value of n will be a valid index of a character in the original string (i.e. n will be in the range 0....len(str)-1 inclusive).

For example:

Test	                                            Result
print(missing_char('kitchen', 1))                   ktchen
print(missing_char('kitchen', 0))                   itchen
print(missing_char('kitchen', 4))                   kitcen
"""
def missing_char(word, n):
  return word.replace(word[n], "")

print(missing_char("kitchen", 1))
print(missing_char('kitchen', 0))
print(missing_char('kitchen', 4))