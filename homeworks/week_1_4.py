# Romans to Integer
#
# Implement a function that can convert a roman numeral into integer.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# [Example 1]
# Input:
# roman = "III"
# Output:
# 3
#
# [Example 2]
# Input:
# roman = "IX"
# Output:
# 9
#
# [Example 3]
# Input:
# roman = "LVIII"
# Output:
# 58
#
# [Example 4]
# Input:
# roman = "MCMXCIV"
# Output:
# 1994

roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
def roman_to_integer(_input: str) -> int:
    s = 0
    for i in _input:
        s += roman[i]
    print(s)
        
roman_to_integer("III")
