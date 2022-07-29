class Solution:
    def romanToInt(self, s: str) -> int:
        roman_List = {'I':1,'IV':4,'V':5,'VI':6,'VII':7,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        j = 0
        numbers = 0
        while(j < len(s)):
            if(j+1 < len(s) and s[j:j+2] in roman_List):
                numbers+=roman_List[s[j:j+2]]
                j+=2
            else:
                numbers+=roman_List[s[j]]
                j+=1
        return numbers
